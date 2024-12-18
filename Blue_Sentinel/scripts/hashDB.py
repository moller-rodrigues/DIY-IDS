import sqlite3 # Imports the sqlite3 library which is an embedded relational database management system

with sqlite3.connect("Signatures.db") as db: # Connects to the database, 'Signatures.db', if it doesn't exist then it is created
    cursor = db.cursor() # Creates a cursor object which is used to traverse the database
    
## Executes a sql query on the database which creates a table called 'user' with the fields: 'userID','username','firstname','surname' and 'password',
## if they do not already exist. 
cursor.execute( '''
CREATE TABLE IF NOT EXISTS hashes(
ID INTEGER PRIMARY KEY,
name VARCHAR(32) NOT NULL,
hash VARCHAR(33) NOT NULL,
cve VARCHAR(32) NOT NULL);
''')

db.commit() # Makes changes made to the database permanent

cursor.execute("SELECT * FROM hashes") # Selects all the data from the table 'hashes'

db.close() # Closes the connection to 'Accounts.db' so that it can be accesed by other processes; avoiding locking of the database.
