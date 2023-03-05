/* Stephen V Input */

INSERT INTO Administers (empId, siteCode) VALUES (1, 258954), (3, 257849), (4, 225489), (6, 234711), (9, 248915);

INSERT INTO Administrator (empId, name, gender) VALUES (1, "Steve", "M"), (3, "Jerry", "M"), (4, "Tom", "M"), (6, "Stan", "M"), (9, "Monica", "F");

INSERT INTO AdmWorkHours (empId, day, hours) VALUES (1, "2023-02-05", 8), (3, "2023-02-06", 8), (4, "2023-02-07", 7), (6, "2023-03-01", 4), (9, "2023-03-02", 12);

INSERT INTO AirtimePackage (packageId, class, startDate, lastDate, frequency, videoCode) VALUES (1, "Red", "2019-01-04", "2019-10-05", 3, 7), (2, "Blue", "2019-03-08", "2019-11-02", 2, 7), (3, "Green", "2020-04-01", "2021-01-08", 6, 4), (4, "Cyan", "2021-07-06", "2022-04-03", 2, 12), (5, "Magenta", "2022-06-03", "2023-03-05", 8, 9);

INSERT INTO Broadcasts (videoCode, siteCode) VALUES (356187, 258954), (355846, 257849), (336482, 225489), (382550, 234711), (344759, 248915);

INSERT INTO Client (clientId, name, phone, address) VALUES (1, "Paul", "575-693-1001", "200 Pensylvania Avenue"), (2, "Randy", "575-407-4892", "581 North Wilson Road"), (3, "Tony", "575-281-5123", "491 Telshor Boulevard"), (4, "Ethan", "575-662-4972", "Quarter Street"), (5, "Keegan", "575-912-5123", "589 Wilkinson Street");

INSERT INTO DigitalDisplay (serialNo, schedulerSystem, modelNo) VALUES (10001, "Mitsubishi", 528764), (10002, "Toshiba", 528664), (10003, "Toyota", 554923), (10004, "Ford", 571986), (10005, "Sega", 593486);

INSERT INTO Locates (serialNo, siteCode) VALUES (10001, 258954), (10002, 257849), (10003, 225489), (10004, 234711), (10005, 248915);

INSERT INTO Purchases (clientId, empId, packageId, commissionRate) VALUES (1, 117542, 1, 140), (2, 154326, 2, 182), (3, 173495, 3, 170), (4, 178359, 4, 360), (5, 189562, 5, 90)

/* Ryan Input */

INSERT INTO Model (modelNo, width, height, depth, screenSize) VALUES (528764, 12, 25, 36, 5, 200), (528664, 12, 25, 36, 5, 240), (554923, 8, 13, 24, 3, 1420), (571986, 20, 35, 48, 2, 1980), (593486, 14, 27, 20, 4, 1280);

INSERT INTO Salesman (empId, name, gender) VALUES (117542, "Beth", "F"), (154326, "Robbie", "M"), (173495, "Mary", "F"), (178359, "Lilth", "F"), (189562, "Tom", "M");

INSERT INTO Site (siteCode, type, address, phone) VALUES (258954, restruant, 1468 S Ave K, 505-849-2566), (257849, dorm, 1527 S Ave O, 505-784-4545), (225489, lobby, 1371 S Ave M, 505-478-5852), (234711, restruant, 1358 S Ave V, 575-488-7452), (248915, lobby, 1784 S Ave M, 505-487-5154);

INSERT INTO Specializes (empId, modelNo) VALUES (134678, 528764), (145787, 554923), (112455, 593486), (134685, 528664), (195239, 571986);

INSERT INTO TechnicalSupport (empId, name, gender) VALUES (112455, "Paul", "M"), (134678, "Joan", "F"), (134685, "Jannet", "F"), (145787, "Billy", "M"), (195239, "Billy", "M");

INSERT INTO Video (videoCode, videoLength) VALUES (356187, 240), (355846, 60), (336482, 270), (382550, 90), (344759, 30);
