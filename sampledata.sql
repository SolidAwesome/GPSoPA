INSERT INTO donation_status (donationstatus) VALUES ('Available');
INSERT INTO donation_status (donationstatus) VALUES ('Not available');
;

INSERT INTO donation_category (category, subcategory, unit, targetgroup)
    VALUES 
        ('Food', 'Canned food', 'kg', 'General'),
        ('Food', 'Dry food', 'kg', 'General'),         
        ('Food', 'Baby food',  'kg', 'Children'), 
        ('Clothing', 'T-shirts', 'piece', 'Male'),
        ('Clothing', 'T-shirts', 'piece', 'Female'),
        ('Clothing', 'T-shirts', 'piece', 'Children'),
        ('Clothing', 'Jackets', 'piece', 'Male'),
        ('Clothing', 'Jackets', 'piece', 'Female'),
        ('Clothing', 'Jackets', 'piece', 'Children'),
        ('Clothing', 'Bottomwear', 'piece', 'Male'),
        ('Clothing', 'Bottomwear', 'piece', 'Female'),
        ('Clothing', 'Bottomwear', 'piece', 'Children'),
        ('Clothing', 'Baby clothes', 'piece', 'Children'),
        ('Shoes', 'Sneakers', 'pair', 'Male'),
        ('Shoes', 'Sneakers', 'pair', 'Female'),
        ('Shoes', 'Sneakers', 'pair', 'Children'),
        ('Shoes', 'Boots', 'pair', 'Male'),
        ('Shoes', 'Boots', 'pair', 'Female'),
        ('Shoes', 'Children shoes', 'pair', 'Children'),
        ('Hygiene Products', 'Soap', 'piece', 'General'),
        ('Hygiene Products', 'Shampoo', 'piece', 'General'),
        ('Hygiene Products', 'Toothpaste', 'piece', 'General'),
        ('Hygiene Products', 'Baby hygiene products', 'piece', 'Children'),
        ('Hygiene Products', 'Menstrual sanitary pads', 'pack' , 'Female')
;

INSERT INTO usertype (userrole)
    VALUES
        ('donor'),
        ('ngo admin'),
        ('admin')
;

INSERT INTO users (username, userrole, contact)
    VALUES 
        ('ana', 1, 'ana.silva@email.com'),
        ('marko', 1, 'marko.lima@email.com'),
        ('sofia', 1, 'sofia.mendes@email.com'),
        ('luka', 1, 'luka.ferreira@email.com'),
        ('mia', 1, 'mia.santos@email.com'),
        ('ivan', 1, 'ivan.rodrigues@email.com'),
        ('lara', 1, 'lara.costa@email.com'),
        ('tiago', 1, 'tiago.alves@email.com'),
        ('nina', 1, 'nina.pinto@email.com'),
        ('bruno', 1, 'bruno.gomes@email.com'),
        ('petra', 1, 'petra.martins@email.com'),
        ('david', 1, 'david.silveira@email.com'),
        ('ines', 1, 'ines.cardoso@email.com'),
        ('miguel', 1, 'miguel.nunes@email.com'),
        ('klara', 1, 'klara.ribeiro@email.com'),
        ('rafael', 1, 'rafael.teixeira@email.com'),
        ('helena', 1, 'helena.moura@email.com'),
        ('tomas', 1, 'tomas.barros@email.com'),
        ('carla', 1, 'carla.duarte@email.com'),
        ('joao', 1, 'joao.fonseca@email.com'),
        ('marija', 1, 'marija.oliveira@email.com'),
        ('andrej', 1, 'andrej.pereira@email.com'),
        ('bianca', 1, 'bianca.fernandes@email.com'),
        ('leo', 1, 'leo.amaral@email.com'),
        ('sara', 1, 'sara.monteiro@email.com')
;

INSERT INTO ngo (ngoname, registrationnumber, contact)
    VALUES
        ('Green Future', 'RN111111', 'contact@greenfuture.org'),
        ('Helping Hands', 'RN111110', 'info@helpinghands.org'),
        ('Hand in Hand', 'RN111100', 'info@handinhand.org')
;

INSERT INTO donation_centers (centername, street, city, postalcode, geolocation)
    VALUES
        ('Central Donation Center', 'Main St 123', 'Lisbon', '1000-001', ST_SetSRID(ST_MakePoint(-9.139, 38.722), 4326)),
        ('North Center', 'North Ave 45', 'Porto', '4000-002', ST_SetSRID(ST_MakePoint(-8.611, 41.149), 4326))
;

INSERT INTO ngo_donationcenters (ngoid, centerid)
    VALUES
        (1, 1),  -- Green Future → Central Donation Center
        (1, 2),  -- Green Future → North Center
        (2, 2)   -- Helping Hands → North Center
;

INSERT INTO events (eventname, eventdescription, ngoid, startdate, enddate, target_categoryid, target_quantity)
    VALUES 
        ('Food January', 'Collecting canned and dry food', 1, '2026-03-01', '2026-03-10', 1, 100);

INSERT INTO sizes (productsize)
    VALUES 
        ('XS'), ('S'), ('M'), ('L'), ('XL'), ('XXL'),
        ('28'), ('30'), ('32'), ('34'), ('36'), 
        ('37'), ('38'), ('39'), ('40'), ('41'), 
        ('42'), ('43'), ('44'), ('45'), ('46')
;

INSERT INTO donations (userid, ngoid, categoryid, sizeid, quantity, centerid, statusid)
    VALUES
        (1, 1, 1, NULL, 10, 1, 1),
        (2, 1, 2, NULL, 5, 1, 1),
        (3, 2, 4, 2, 3, 2, 1)
;  