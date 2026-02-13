
CREATE DATABASE sustainable_donation;
SET search_path TO donation;

CREATE TABLE donation_status (
    statusid SERIAL PRIMARY KEY,
    donationstatus VARCHAR(50) NOT NULL UNIQUE
);

CREATE TABLE donation_category (
    categoryid SERIAL PRIMARY KEY,
    category VARCHAR(100) NOT NULL,
    specification TEXT NOT NULL,
    unit VARCHAR(20) NOT NULL,
    targetgroup VARCHAR(100),
    UNIQUE (category, targetgroup)
);

CREATE TABLE users (
    userid SERIAL PRIMARY KEY,
    username VARCHAR(10) NOT NULL,
    contact VARCHAR(100) NOT NULL UNIQUE,
    userrole VARCHAR(20) NOT NULL CHECK (position IN ('donor', 'ngoadmin', 'admin')),
    created TIMESTAMP DEFAULT NOW()
);

CREATE TABLE ngo (
    ngoid INT PRIMARY KEY,
    ngoname VARCHAR(150) NOT NULL UNIQUE
);

CREATE TABLE donation_centers (
    centerid SERIAL PRIMARY KEY,
    centername VARCHAR(150) NOT NULL,
    street VARCHAR(150) NOT NULL,
    city VARCHAR(100) NOT NULL,
    postalcode VARCHAR(15) NOT NULL,
    geolocation GEOGRAPHY NOT NULL
);

CREATE TABLE events (
    eventid SERIAL PRIMARY KEY,
    eventname VARCHAR(150) NOT NULL,
    eventdescription TEXT,
    ngoid INT NOT NULL
        REFERENCES ngo(ngoid)
            ON DELETE CASCADE,
    startdate DATETIME NOT NULL,
    enddate DATE,
    target_categoryid INT NOT NULL
        REFERENCES donation_category(categoryid),
    target_quantity INT CHECK (target_quantity >= 0)
);

CREATE TABLE donations (
    id SERIAL PRIMARY KEY,
    userid INT NOT NULL REFERENCES users(userid),
    ngoid INT NOT NULL REFERENCES ngo(ngoid),
    categoryid INT NOT NULL REFERENCES donation_category(categoryid),
    quantity INT NOT NULL CHECK (quantity > 0),
    centerid INT REFERENCES donation_centers(centerid),
    eventid INT REFERENCES events(eventid),
    statusid INT NOT NULL REFERENCES donation_status(statusid),
    donationdate TIMESTAMP DEFAULT NOW()
);