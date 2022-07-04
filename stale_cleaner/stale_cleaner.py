import mysql.connector

mydb = mysql.connector.connect(
  host="192.168.56.23",
  port=32001,
  user="root",
  password=""
)
 
print(mydb)
#
# CREATE TABLE test.usersubs (
# 	subid INT NOT NULL,
# 	partner varchar(10) NULL,
# 	status varchar(10) NULL,
# 	enddate DATE NULL
# )
# ENGINE=InnoDB
# DEFAULT CHARSET=latin1
# COLLATE=latin1_swedish_ci;

# SELECT * FROM test.usersubs u ;
# INSERT INTO test.usersubs (subid, partner, status, enddate) VALUES (101, 'zee5', 'ACTIVE', DATE_SUB(CURDATE(), INTERVAL 6 DAY));
# INSERT INTO test.usersubs (subid, partner, status, enddate) VALUES (102, 'hotstar', 'ACTIVE', sysdate());
# commit;
