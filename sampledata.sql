INSERT INTO donation_status (statusid, donationstatus) 
    VALUES (1, 'Available'
            2, 'Not available')
;

INSERT INTO donation_category (categoryid, category, specification, unit, targetgroup)
    VALUES (1, 'Food', 'Canned food', 'kg', 'General'),
            (2, 'Food', 'Dry food', 'kg', 'General'
            3, 'Food', 'Baby food',  'kg', 'Children'
            4, 'Clothing', 'T-shirts', 'piece', 'Male'
            5, 'Clothing', 'T-shirts', 'piece', 'Female'
            6, 'Clothing', 'Jackets', 'piece', 'Male'
            7, 'Clothing', 'Jackets', 'piece', 'Female'
            8, 'Clothing', 'Children clothing', 'piece', 'Children'
            9, 'Shoes', 'Sneakers', 'pair', 'Male'
            10, 'Shoes', 'Sneakers', 'pair', 'Female'
            11, 'Shoes', 'Boots', 'pair', 'Male'
            12, 'Shoes', 'Boots', 'pair', 'Female'
            13, 'Shoes', 'Children shoes', 'pair', 'Children'
            14, 'Hygiene Products', 'Soap', 'piece', 'General'
            15, 'Hygiene Products', 'Shampoo', 'piece', 'General'
            16, 'Hygiene Products', 'Toothpaste', 'piece', 'General'
            17, 'Hygiene Products', 'Baby hygiene products', 'piece', 'Children'
            18, 'Hygiene Products', 'Menstrual sanitary pads', 'pack' , 'Female')
            ;