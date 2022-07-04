show tables;
SELECT * FROM test.datetest;
desc test.datetest;
INSERT into test.datetest (enddate) values (sysdate());
INSERT into test.datetest (enddate) values (sysdate());
INSERT into test.datetest (enddate) values (DATE_SUB(CURDATE(), INTERVAL 6 DAY) );

SELECT * FROM test.usersubs u ;

INSERT INTO test.usersubs (subid, partner, status, enddate) VALUES (101, 'zee5', 'ACTIVE', DATE_SUB(CURDATE(), INTERVAL 6 DAY));
INSERT INTO test.usersubs (subid, partner, status, enddate) VALUES (102, 'hotstar', 'ACTIVE', sysdate());
INSERT INTO test.usersubs (subid, partner, status, enddate) VALUES (103, 'balaji', 'ACTIVE', DATE_SUB(CURDATE(), INTERVAL 3 DAY));
INSERT INTO test.usersubs (subid, partner, status, enddate) VALUES (104, 'shemaroo', 'ACTIVE', DATE_SUB(CURDATE(), INTERVAL 1 DAY));
commit;



