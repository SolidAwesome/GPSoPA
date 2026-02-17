INSERT INTO units (unitname) 
    VALUES ('g'), ('kg'), ('piece'), ('pair'), ('pack')
;
 
INSERT INTO target_groups (groupname) 
    VALUES ('General'), ('Male'), ('Female'), ('Children'), ('Baby')
;

INSERT INTO categories (categoryname) 
    VALUES ('Food'), ('Clothing'), ('Shoes'), ('Hygiene Products'), ('Household')
;

INSERT INTO subcategories (subcategoryname, categoryid) 
    VALUES
        ('Canned Food', 1),
        ('Dry Food', 1),
        ('Baby Food', 1),
        ('Cooking Oil', 1),
        ('Spices', 1),
        ('Snacks', 1);
INSERT INTO subcategories (subcategoryname, categoryid) 
    VALUES
        ('T-shirts', 2),
        ('Jackets', 2),
        ('Trousers', 2),
        ('Sweaters', 2),
        ('Dresses', 2),
        ('Coats', 2),
        ('Socks', 2),
        ('Underwear', 2),
        ('Scarves & Gloves', 2),
        ('Baby Clothes', 2);
INSERT INTO subcategories (subcategoryname, categoryid) 
    VALUES
        ('Sneakers', 3),
        ('Boots', 3),
        ('Sandals', 3),
        ('Formal Shoes', 3),
        ('Flip Flops', 3);
INSERT INTO subcategories (subcategoryname, categoryid) 
    VALUES
        ('Soap', 4),
        ('Shampoo', 4),
        ('Toothpaste', 4),
        ('Baby Hygiene Products', 4),
        ('Menstrual Pads', 4),
        ('Toothbrushes', 4),
        ('Deodorant', 4),
        ('Wet Wipes', 4),
        ('Hand Sanitizer', 4),
        ('Razors', 4);
INSERT INTO subcategories (subcategoryname, categoryid) 
    VALUES
        ('Blankets', 5),
        ('Towels', 5),
        ('Kitchenware', 5),
        ('Bedding Sets', 5),
        ('Cleaning Supplies', 5),
        ('Pots & Pans', 5),
        ('Plates & Cups', 5),
        ('Laundry Detergent', 5),
        ('Small Appliances', 5),
        ('Pillows', 5);

INSERT INTO donation_items (subcategoryid, unitid, targetgroupid) 
    VALUES
        (1, 2, 1),
        (2, 2, 1),
        (3, 2, 5),
        (4, 2, 1),
        (5, 2, 1),
        (6, 2, 1);
INSERT INTO donation_items (subcategoryid, unitid, targetgroupid) 
    VALUES
        (7, 3, 2),
        (7, 3, 3),
        (7, 3, 4),
        (8, 3, 2),
        (8, 3, 3),
        (8, 3, 4),
        (9, 3, 2),
        (9, 3, 3),
        (9, 3, 4),
        (10, 3, 2),
        (10, 3, 3),
        (10, 3, 4),
        (11, 3, 3),
        (11, 3, 4), 
        (12, 3, 2),
        (12, 3, 3),
        (12, 3, 4),
        (13, 3, 2),
        (13, 3, 3),
        (13, 3, 4),
        (14, 3, 2),
        (14, 3, 3),
        (14, 3, 4),
        (15, 3, 2),
        (15, 3, 3),
        (15, 3, 4),
        (16, 3, 5);
INSERT INTO donation_items (subcategoryid, unitid, targetgroupid) 
VALUES
        (17, 4, 2),
        (17, 4, 3),
        (17, 4, 4),
        (18, 4, 2),
        (18, 4, 3),
        (18, 4, 4),
        (19, 4, 2),
        (19, 4, 3),
        (19, 4, 4),
        (20, 4, 2),
        (20, 4, 3),
        (21, 4, 2),
        (21, 4, 3),
        (21, 4, 4);
INSERT INTO donation_items (subcategoryid, unitid, targetgroupid) 
    VALUES
        (22, 3, 1),
        (23, 3, 1),
        (24, 3, 1),
        (25, 3, 5),
        (26, 5, 3),
        (27, 3, 1),
        (28, 3, 1),
        (29, 3, 1),
        (30, 3, 1),
        (31, 3, 1);
INSERT INTO donation_items (subcategoryid, unitid, targetgroupid) 
    VALUES
        (32, 3, 1),
        (33, 3, 1),
        (34, 3, 1),
        (35, 3, 1),
        (36, 3, 1),
        (37, 3, 1),
        (38, 3, 1),
        (39, 3, 1),
        (40, 3, 1),
        (41, 3, 1)
;

INSERT INTO donation_status (donationstatus) 
    VALUES ('Available'), ('Reserved'), ('Collected')
;

INSERT INTO usertype (userrole)
    VALUES ('donor'), ('NGO admin'), ('admin')
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

INSERT INTO ngo_center (ngoid, centerid)
    VALUES (1, 1), (1, 2), (2, 2)
;

INSERT INTO events (eventname, eventdescription, ngoid, startdate, enddate, eventtarget, quantitytarget)
    VALUES
        ('Clothing April', 'T-shirts, jackets, trousers and baby clothes', 1, '2026-04-05', '2026-04-15', 7, 150),
        ('Shoes Collection May', 'Sneakers, boots, sandals for all', 1, '2026-05-01', '2026-05-10', 17, 100),
        ('Hygiene June', 'Soap, shampoo, toothpaste, pads', 1, '2026-06-01', '2026-06-10', 22, 120);
        ('Spring Food Drive', 'Rice, pasta, cooking oil and spices', 2, '2026-03-15', '2026-03-25', 1, 150)
;

INSERT INTO sizes (productsize)
    VALUES 
        ('XS'), ('S'), ('M'), ('L'), ('XL'), ('XXL'),
        ('28'), ('30'), ('32'), ('34'), ('36'), 
        ('37'), ('38'), ('39'), ('40'), ('41'), 
        ('42'), ('43'), ('44'), ('45'), ('46')
;

INSERT INTO donations (userid, ngocenterid, itemid, sizeid, quantity, donationdescription, eventid, statusid)
    VALUES
        (1, 3, 1, NULL, 15, 'Canned food donation', 4, 1),
        (2, 3, 2, NULL, 20, 'Dry food donation', 4, 1),
        (6, 3, 3, NULL, 8, 'Baby food donation', 4, 1),
        (3, 1, 7, 2, 5, 'T-shirts Male', 1, 1),
        (4, 1, 8, 3, 3, 'Jackets Female', 1, 2),
        (5, 1, 9, 2, 4, 'Trousers Male', 1, 1),
        (10, 1, 25, NULL, 6, 'Baby Clothes', 1, 1),
        (7, 1, 17, 41, 2, 'Sneakers Male', 2, 1),
        (8, 1, 18, 42, 3, 'Boots Female', 2, 1),
        (9, 1, 19, 40, 2, 'Sandals Children', 2, 1),
        (11, 1, 22, NULL, 12, 'Soap donation', 3, 1),
        (12, 1, 23, NULL, 8, 'Shampoo donation', 3, 1),
        (13, 1, 25, NULL, 6, 'Baby Hygiene Products', 3, 1),
        (14, 1, 24, NULL, 5, 'Toothpaste donation', 3, 1)
;