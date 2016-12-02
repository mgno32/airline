#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os, sys, string
import MySQLdb

#todo
#changeflight:
#change_flightid()
#change_company()
#change_flight_name()
#change_dept_name()
#change_arrv_name()
#change_seat()
#change_price()

#add_flight()
#change all

#delete_flight()

#search_flight:
#search
def connect():
	global curAdmin
	global connAdmin
	try:
		connAdmin = MySQLdb.connect(host='127.0.0.1',user='root',passwd='',db='airline',charset='utf8')
        curAdmin = connAdmin.cursor() 
		
	except Exception, e:
		print e
		sys.exit()


