"""
ETL script for donation_centers table in the database.

Extracts all supermarket locations in Lisbon from OpenStreetMap using hte Overpass API, which we will consider for the duration of the project as viable locations where NGOs can pick up donations (can be further changed into a live table updated by NGOs with actual locations they choose);
transforms the information into our predetermined fields, and loads them into the table
donation.donation_centers in our PostgreSQL server.
"""

import os
import requests
import psycopg2

# Overpass API connection
OVERPASS_URL = "https://overpass-api.de/api/interpreter"

# Overpass query: supermarkets inside the Lisbon administrative area
OVERPASS_QUERY = r"""
[out:json];
area["name"="Lisboa"]["boundary"="administrative"]->.a;
(
  node["shop"="supermarket"](area.a);
);
out center;
"""


# Database settings - basic defaults
DB_SETTINGS = {
    "dbname": "sustainable_donation",
    "user": "postgres",
    "host": "localhost",
    "port": "5432"
}

def fetch_supermarkets():
    """
    Extract.

    Calls the Overpass API and returns a list of supermarket elements
    (only nodes with shop=supermarket identifier) in Lisbon.
    """
    response = requests.post(
        OVERPASS_URL,
        data={"data": OVERPASS_QUERY},
        timeout=120
    )
    response.raise_for_status()
    data = response.json()
    return data.get("elements", [])


def run_etl():
    """
    Main ETL function.

    - Extract: get supermarket data from Overpass
    - Transform: adapt OSM tags to our table columns
    - Load: insert rows into donation.donation_centers
    """
    supermarkets = fetch_supermarkets()
    print(f"Extracted {len(supermarkets)} supermarkets from OpenStreetMap.")

    # Connect to PostgreSQL
    conn = psycopg2.connect(**DB_SETTINGS)
    cur = conn.cursor()

    inserted = 0

    for el in supermarkets:
        # Each element is a node with tags and coordinates and skip ones without location data
        tags = el.get("tags", {})
        lon = el.get("lon")
        lat = el.get("lat")

        if lon is None or lat is None:
            continue  

        # Transform: build our fields from OSM tags
        centername = tags.get("name", f"Supermarket {el.get('id', '')}")
        street = tags.get("addr:street", "")
        city = tags.get("addr:city", "Lisbon")
        postalcode = tags.get("addr:postcode", "0000-000")

        # Load: insert into donation_centers
        cur.execute(
            """
            INSERT INTO donation.donation_centers
            (centername, street, city, postalcode, geolocation)
            VALUES (%s, %s, %s, %s, ST_SetSRID(ST_MakePoint(%s, %s), 4326))
            ON CONFLICT DO NOTHING;
            """,
            (centername, street, city, postalcode, lon, lat)
        )
        inserted += cur.rowcount

    conn.commit()
    cur.close()
    conn.close()

    print(f"Inserted {inserted} new donation centers.")


if __name__ == "__main__":
    run_etl()
