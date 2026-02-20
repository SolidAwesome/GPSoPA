
CREATE DATABASE sustainable_donation;
CREATE SCHEMA IF NOT EXISTS donation;
SET search_path TO donation;
DROP SCHEMA IF EXISTS donation CASCADE;
CREATE SCHEMA donation;  
CREATE EXTENSION IF NOT EXISTS postgis;

CREATE TABLE units (
    unitid SERIAL PRIMARY KEY,
    unitname VARCHAR(20) NOT NULL UNIQUE
);

CREATE TABLE target_groups (
    targetgroupid SERIAL PRIMARY KEY,
    groupname VARCHAR(50) NOT NULL UNIQUE
);

CREATE TABLE categories (
    categoryid SERIAL PRIMARY KEY,
    categoryname VARCHAR(100) NOT NULL UNIQUE
);

CREATE TABLE subcategories (
    subcategoryid SERIAL PRIMARY KEY,
    subcategoryname VARCHAR(300) NOT NULL,
    categoryid INT NOT NULL REFERENCES categories(categoryid) ON DELETE CASCADE,
    UNIQUE (subcategoryname, categoryid)
);

CREATE TABLE donation_items (
    itemid SERIAL PRIMARY KEY,
    subcategoryid INT NOT NULL REFERENCES subcategories(subcategoryid) ON DELETE RESTRICT,
    unitid INT NOT NULL REFERENCES units(unitid) ON DELETE RESTRICT,
    targetgroupid INT NOT NULL REFERENCES target_groups(targetgroupid) ON DELETE RESTRICT,
    UNIQUE (subcategoryid, targetgroupid)
);

CREATE TABLE donation_status (
    statusid SERIAL PRIMARY KEY,
    donationstatus VARCHAR(50) NOT NULL UNIQUE
);

CREATE TABLE usertype (
    usertypeid SERIAL PRIMARY KEY,
    userrole VARCHAR(20) NOT NULL UNIQUE
);

CREATE TABLE users (
    userid SERIAL PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    userrole INT NOT NULL REFERENCES usertype(usertypeid),
    contact VARCHAR(100) NOT NULL UNIQUE,
    created DATE DEFAULT NOW()
);

CREATE TABLE ngo (
    ngoid SERIAL PRIMARY KEY,
    ngoname VARCHAR(150) NOT NULL UNIQUE,
    registrationnumber VARCHAR(100) NOT NULL UNIQUE,
    contact VARCHAR(100) NOT NULL UNIQUE
);

CREATE TABLE donation_centers (
    centerid SERIAL PRIMARY KEY,
    centername VARCHAR(150) NOT NULL,
    street VARCHAR(150) NOT NULL,
    city VARCHAR(100) NOT NULL,
    postalcode VARCHAR(15) NOT NULL,
    geolocation GEOMETRY(POINT,4326) NOT NULL
);

CREATE TABLE ngo_center (
    ngocenterid SERIAL PRIMARY KEY,
    ngoid INT NOT NULL REFERENCES ngo(ngoid) ON DELETE CASCADE,
    centerid INT NOT NULL REFERENCES donation_centers(centerid) ON DELETE CASCADE,
    UNIQUE (ngoid, centerid)
);

CREATE TABLE events (
    eventid SERIAL PRIMARY KEY,
    eventname VARCHAR(150) NOT NULL,
    eventdescription VARCHAR(150),
    ngoid INT NOT NULL REFERENCES ngo(ngoid) ON DELETE CASCADE,
    startdate DATE NOT NULL,
    enddate DATE,
    eventtarget INT NOT NULL REFERENCES donation_items(itemid),
    quantitytarget INT NOT NULL CHECK (quantitytarget >= 0)
);

CREATE TABLE sizes (
    sizeid SERIAL PRIMARY KEY,
    productsize VARCHAR(10) NOT NULL UNIQUE
);

CREATE TABLE donations (
    id SERIAL PRIMARY KEY,
    userid INT NOT NULL REFERENCES users(userid),
    ngocenterid INT NOT NULL REFERENCES ngo_center(ngocenterid),
    itemid INT NOT NULL REFERENCES donation_items(itemid),
    sizeid INT REFERENCES sizes(sizeid),
    quantity INT NOT NULL CHECK (quantity > 0),
    donationdescription VARCHAR(150),
    eventid INT REFERENCES events(eventid),
    statusid INT NOT NULL REFERENCES donation_status(statusid),
    donationdate DATE DEFAULT NOW()
);