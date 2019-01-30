#!/usr/bin/env python

from _pybgpstream import BGPStream, BGPRecord, BGPElem
import time
import datetime
import ciso8601

print '\n\n-----------------  Welcome to the DDoS Observatory  -----------------\n\n'

# Create a new bgpstream instance and a reusable bgprecord instance
stream = BGPStream()
rec = BGPRecord()

# Consider RIPE RRC (Remote Route Collector) 10 only            ############################ is there a better way to write this code?
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

# User Inputs Time Intervals - Starting and timestamps
# User enters date in DD/MM/YY format and it is converted to int format.
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

# Time interval:
stream.add_interval_filter(int(startTime),int(endTime))

# Start the stream
stream.start()
print "\n"
print "---------------------------------------------------------------------------------------------------"
print "|                         Record                       |                    Element                |"
print "---------------------------------------------------------------------------------------------------"			
print "| Project | Collector |  Type  |    Time    |  Status  | Type |  Peer Address  | Peer ASN | Fields |"
# Get next record
while(stream.get_next_record(rec)):
    # Print the record information only if it is not a valid record
    if rec.status != "valid":
	print "--THIS IS AN INVALID RECORD--"
	print '| {:6s} | {:9s} | {:6s} | {:10d} | {:8s} '.format(rec.project, rec.collector, rec.type, rec.time, rec.status)
	print "-----------------------------"
    else:
        elem = rec.get_next_elem()
        while(elem):
		#if it contains :, if it's a IPv6, then don't include it
		 #AND the word prefix is contained within the element fields
		  #AND only include records with larger than /24 prefixes
		if ":" not in elem.peer_address and 'prefix' in elem.fields and int(elem.fields['prefix'].split("/")[1]) >= 24:
			# Print record and elem information
			print '| {:6s} | {:9s} | {:6s} | {:10d} | {:8s} '.format(rec.project, rec.collector, rec.type, rec.time, rec.status),
			#print "| " + rec.project + " | " + rec.collector + " | " + rec.type + " | ", rec.time , " | " + rec.status+ " | ",
			print '| {:4s} | {:14s} | {:8d} |'.format(elem.type, elem.peer_address, elem.peer_asn),#, elem.fields, " |"
			print elem.fields['prefix']
		elem = rec.get_next_elem()
