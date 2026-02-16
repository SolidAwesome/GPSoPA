
CREATE DATABASE sustainable_donation;
SET search_path TO donation;

DROP TABLE IF EXISTS donation_status;

CREATE TABLE donation_status (
    statusid SERIAL PRIMARY KEY,
    donationstatus VARCHAR(50) NOT NULL UNIQUE
);

DROP TABLE IF EXISTS donation_category;

CREATE TABLE donation_category (
    categoryid SERIAL PRIMARY KEY,
    category VARCHAR(100) NOT NULL,
    subcategory VARCHAR(300) NOT NULL,
    unit VARCHAR(20) NOT NULL,
    targetgroup VARCHAR(100),
    UNIQUE (category, subcategory, targetgroup)
);

DROP TABLE IF EXISTS usertype;

CREATE TABLE usertype (
    usertypeid SERIAL PRIMARY KEY,
    userrole VARCHAR(20) NOT NULL
);

DROP TABLE IF EXISTS users;

CREATE TABLE users (
    userid SERIAL PRIMARY KEY,
    username VARCHAR(10) NOT NULL,
    userrole INT NOT NULL REFERENCES usertype(usertypeid),
    contact VARCHAR(100) NOT NULL UNIQUE,
    created DATE DEFAULT NOW()
);

DROP TABLE IF EXISTS ngo;

CREATE TABLE ngo (
    ngoid SERIAL PRIMARY KEY,
    ngoname VARCHAR(150) NOT NULL UNIQUE,
    registrationnumber VARCHAR(100) NOT NULL UNIQUE,
    contact VARCHAR(100) NOT NULL UNIQUE
);

DROP TABLE IF EXISTS donation_centers;

CREATE TABLE donation_centers (
    centerid SERIAL PRIMARY KEY,
    centername VARCHAR(150) NOT NULL,
    street VARCHAR(150) NOT NULL,
    city VARCHAR(100) NOT NULL,
    postalcode VARCHAR(15) NOT NULL,
    geolocation GEOMETRY(POINT,4326) NOT NULL
);

DROP TABLE IF EXISTS ngo_donationcenters;

CREATE TABLE ngo_donationcenters (
    id SERIAL PRIMARY KEY,
    ngoid INT REFERENCES ngo(ngoid) NOT NULL,
    centerid INT REFERENCES donation_centers(centerid) NOT NULL
);

DROP TABLE IF EXISTS events;

CREATE TABLE events (
    eventid SERIAL PRIMARY KEY,
    eventname VARCHAR(150) NOT NULL,
    eventdescription TEXT,
    ngoid INT NOT NULL
        REFERENCES ngo(ngoid)
            ON DELETE CASCADE,
    startdate DATE NOT NULL,
    enddate DATE,
    target_categoryid INT NOT NULL
        REFERENCES donation_category(categoryid),
    target_quantity INT CHECK (target_quantity >= 0)
);

DROP TABLE IF EXISTS sizes;

CREATE TABLE sizes (
    sizeid SERIAL PRIMARY KEY,
    productsize VARCHAR (10) NOT NULL UNIQUE
);

DROP TABLE IF EXISTS donations;

CREATE TABLE donations (
    id SERIAL PRIMARY KEY,
    userid INT NOT NULL REFERENCES users(userid),
    ngoid INT NOT NULL REFERENCES ngo(ngoid),
    categoryid INT NOT NULL REFERENCES donation_category(categoryid),
    sizeid INT REFERENCES sizes(sizeid),
    quantity INT NOT NULL CHECK (quantity > 0),
    centerid INT REFERENCES donation_centers(centerid),
    eventid INT REFERENCES events(eventid),
    statusid INT NOT NULL REFERENCES donation_status(statusid),
    donationdate DATE DEFAULT NOW()
);