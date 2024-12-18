import sqlite3
import os


def add_malware_signaure(name, hashVal, cve = None):
    with sqlite3.connect("Signatures.db") as  db: # Connects to the fileHashes database
        cursor = db.cursor() #  Creates cursor object to traverse through the database
        findHash = ("SELECT * FROM hashes WHERE hash = ?") # SQL query to check if that signature already exists
        cursor.execute(findHash,[(hashVal)])

        # if exists return else add to DB
        if cursor.fetchall():
            return
        else:
            insertData = '''INSERT INTO hashes (name,hash,cve) 
                    VALUES(?,?,?)'''
            cursor.execute(insertData,[(name),(hashVal), (cve)])
            db.commit() # Makes changes made to the database permanent

def get_hash_list():
    hashes = []
    with sqlite3.connect("Signatures.db") as  db: # Connects to the fileHashes database
        cursor = db.cursor() #  Creates cursor object to traverse through the database
        getHashes = ("SELECT hash from hashes") # SQL query to check if that signature already exists
        cursor.execute(getHashes)

        for h in cursor.fetchall():
            for x in h:
                hashes.append(x)
    db.commit() # Makes changes made to the database permanent
    return hashes



#add_malware_signaure("customMalware", "54b0c58c7ce9f2a8b551351102ee0938", "CVE CUSTOM")
#get_hash_list()