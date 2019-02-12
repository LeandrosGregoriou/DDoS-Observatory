#!/usr/bin/env python

from _pybgpstream import BGPStream, BGPRecord, BGPElem
import sys
import time
import datetime
import ciso8601
import mysql.connector
from mysql.connector import errorcode
import MySQLdb
import sys






def insertRecord(prefix, prefixLength, asPAth, BGPcommunities, 
				nextHop, collector, timestamp):
				
				db = MySQLdb.connect(host="localhost",    # your host, usually localhost
						     user="root",         # your username
						     passwd="password",  # your password
						     db="RecordsDB")        # name of the data base
				cursor = db.cursor()

				if cursor.lastrowid():
					recordID = cursor.lastrowid() + 1
				else:
					recordID = 1;
				
				
				query = "INSERT INTO recordsTable(recordID, prefix, prefixLength, asPAth, \
						 BGPcommunities, nextHop, collector, timestamp)  \
							VALUES (%s, %s, %s, %s, %s, %s, %s, %s)" 
						
				args = (recordID, prefix, prefixLength, asPAth, BGPcommunities, nextHop, collector, timestamp)
				
				cursor.execute(query, args)

				db.commit()

				db.close()




print '\n\n-----------------  Welcome to the DDoS Observatory  -----------------\n\n'

# Create a new bgpstream instance and a reusable bgprecord instance
stream = BGPStream()
rec = BGPRecord()

start_date = sys.argv[1]
end_date = sys.argv[2]
startTime = time.mktime(ciso8601.parse_datetime(start_date).timetuple()) # pip install ciso8601
endTime = time.mktime(ciso8601.parse_datetime(end_date).timetuple())

 #Consider RIPE RRC (Remote Route Collector) # if not specified it will omit all the collectors
'''
stream.add_filter('collector','rrc00') # Amsterdam
stream.add_filter('collector','rrc01') # London
stream.add_filter('collector','rrc02') # Paris, France
stream.add_filter('collector','rrc03') # Amsterdam
stream.add_filter('collector','rrc04') # Geneva
stream.add_filter('collector','rrc05') # Vienna
stream.add_filter('collector','rrc06') # Otemachi
stream.add_filter('collector','rrc07') # Stockholm
stream.add_filter('collector','rrc08') # San Jose (CA), USA
stream.add_filter('collector','rrc09') # Zurich, Switzerland
stream.add_filter('collector','rrc10') # Milan, Italy
stream.add_filter('collector','rrc11') # NY USA
stream.add_filter('collector','rrc12') # Frankfurt, Germany
stream.add_filter('collector','rrc13') # Moscow, Russia
stream.add_filter('collector','rrc14') # Palo Alto, USA
stream.add_filter('collector','rrc15') # Sao Paulo, Brazil
stream.add_filter('collector','rrc16') # Miami, USA
stream.add_filter('collector','rrc18') # Barcelona, Spain.
stream.add_filter('collector','rrc19') # Johannesburg, South Africa
stream.add_filter('collector','rrc20') # Zurich, Switzerland
stream.add_filter('collector','rrc21') # Paris, France
stream.add_filter('collector','rrc22') # Bucharest, Romania
stream.add_filter('collector','rrc23') # Singapore
'''
stream.add_filter('project', 'ris')

# User Inputs Time Intervals - Starting and timestamps
# User enters date in DD/MM/YY format and it is converted to int format.
'''
isValid=False
while not isValid:
	userIn = raw_input("Please provide the starting date in the format 'YYYY-MM-DD'.\n")
	try: 
		startTime = time.mktime(ciso8601.parse_datetime(userIn).timetuple()) # pip install ciso8601    
		isValid=True
	except:
		print "Try again!\n"

isValid=False
while not isValid:
	userIn = raw_input("Please provide the ending date in the format 'YYYY-MM-DD'.\n")
	try: 
		endTime = time.mktime(ciso8601.parse_datetime(userIn).timetuple())
		isValid=True
	except:
		print "Try again!\n"
'''
# Time interval:
stream.add_interval_filter(int(startTime),int(endTime))

# Start the stream
stream.start()
print "\n"
print "----------------------------------------------------------------------------------------------------------------"
print "|                         Record                       |                         Element                       |"
print "----------------------------------------------------------------------------------------------------------------"			
print "| Project | Collector |  Type  |    Time    |  Status  | Type |  Peer Address  | Peer ASN |       Prefix       |"

#for building up purposes im only allowing 100 records to be collected
i = 0
while (i<100):
	# Get next record
	# while(stream.get_next_record(rec)):
	stream.get_next_record(rec)
	# Print the record information only if it is not a valid record
	if rec.status != "valid":
		#print "--INVALID RECORD--"
		print '| {:6s} | {:9s} | {:6s} | {:10d} | {:8s} '.format(rec.project, rec.collector, rec.type, rec.time, rec.status)
		#print "-----------------------------"
	else:
		elem = rec.get_next_elem()
		while(elem):
			#if it contains :, if it's a IPv6, then don't include it
			#AND the word prefix is contained within the element fields
			#AND only include records with larger than /24 prefixes
			if ":" not in elem.peer_address and 'prefix' in elem.fields and int(elem.fields['prefix'].split("/")[1]) > 24:
				# Print record and elem information
				print '|  {:6s} | {:9s} | {:6s} | {:10d} | {:8s} '.format(rec.project, rec.collector, rec.type, rec.time, rec.status),
				print '| {:4s} | {:14s} | {:8d} | {:18s} |'.format(elem.type, elem.peer_address, elem.peer_asn, elem.fields['prefix'])#, elem.fields, " |"
				
				insertRecord(str(elem.fields['prefix']), elem.fields['prefix'].split("/")[1],\
						str(elem.fields['as-path']), str(elem.fields['communities']), str(elem.fields['next-hop']), rec.collector, rec.time)
				i = i + 1
			elem = rec.get_next_elem()
			

print ("Completed logging 100 records.")
