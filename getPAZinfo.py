#!/bin/env python

''' fetch the resp paz for full-frequency response email '''

from obspy.io.xseed import Parser
from obspy.core.inventory.response import Response
from obspy.core.inventory import read_inventory
# do i need to import the obspy inventory reader?  what does austin do? he has his own resp utils
from obspy import UTCDateTime

station='SFJD'
network='IU'
channel='BHZ'
location='10'

# this has more than one volume index control header found and doesn't work
#respFile="/dcc/metadata/dataless/DATALESS."+network+"_"+station+".seed"

# this seems to work, but then you have to search for station.
# it will also give warnings about more than one abbreviation control header found...
respFile='/APPS/metadata/SEED/'+network+'.dataless'

#create and inventory of the dataless resp info
respIn=Parser(respFile)
inv = respIn.get_inventory()
nslc=network+'.'+station+'.'+location+'.'+channel

#print(inv.keys())
#dict_keys(['channels', 'networks', 'stations'])
#print(inv.values())
#print(inv.items())

for ch in inv['channels']:
    if(ch['channel_id']==nslc):
      print(ch['channel_id'])
      print(Response(desc=ch['channel_id']))
      #print(ch.get_paz)


####
#'''Traceback (most recent call last):
#  File "getPAZinfo.py", line 28, in <module>
#    print(ch.get_paz)
##AttributeError: 'dict' object has no attribute 'get_paz''''
