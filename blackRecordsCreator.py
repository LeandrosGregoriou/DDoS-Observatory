import mysql.connector
from mysql.connector import errorcode
import MySQLdb
from ast import literal_eval

blackholedRec = open("blackholedRecords.txt", "w")
blackholedRec.write("The following are the blackholed record IDs: \n")
try:
    db = MySQLdb.connect(host="localhost",          # host
                                user="root",       # username
                                passwd="password", # password
                                db="RecordsDB")    # name of the data base
    sql_select_Query = "SELECT * FROM recordsTable"
    cursor = db .cursor()
    cursor.execute(sql_select_Query)
    databaseRows = cursor.fetchall()

    #put all blackholing dictionaries in a set
    blackSet = set(({}))
    filepath = 'blackCommfile.txt'
    with open(filepath) as fp:  
        line = fp.readline()
        cnt = 1
        while line:
            blackSet.add(line.strip())
            line = fp.readline()
            cnt += 1

    #iterate through each row in database
    for row in databaseRows:
        #record ID
        recordID = row[0]
        #convert communities string to dictionary
        commsDictionary = literal_eval(row[4])
        #convert communites in correct format - from {'asn': 3549, 'value': 666} to '3549:666'
        rowCommunities = []
        for c in commsDictionary:
            community = "{}:{}".format(c['asn'], c['value'])
            rowCommunities.append(community)
     
        #iterate through each community in the row of communities
        for rowComm in rowCommunities:
            #iterate through the blackholing communities set
            for blackComm in blackSet:
                #check comunity is equal to blackholing community
                if (rowComm == blackComm):
                    print("Blackholed Record FOUND! ID:", recordID)
                    blackholedRec.write(str(recordID) + "\n")

    cursor.close()

except errorcode as e :
    print ("Error while connecting to MySQL", e)
finally:
    db.close()
    print("MySQL connection closed")