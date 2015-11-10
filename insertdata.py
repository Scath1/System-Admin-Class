import sqlite3


conn = sqlite3.connect("test.db")

print "Opened database successfully"


conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
	VALUES (1, 'PAUL', 32, 'CALIFORNIA', 20000.00 )")

conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
	VALUES (2, 'ALAN', 25, 'TEXAS', 15000.00 )")

conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
	VALUES (3, 'TEDDY', 23, 'NORWAY', 20000.00 )")

conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
	VALUES (4, 'MARK', 25, 'RICH-MOND', 65000.00 )")


conn.commit()

print "Records created successfully";

conn.close()