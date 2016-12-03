#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os, sys, string
import MySQLdb
import administor_os

administor_login.connect()
administor_os.connect()

admin_id = administor_login.admin_log_in("123@126.com","125")
#1.show all price info
result = administor_os.show_all_price_info()

#2.show all flight info
result = administor_os.show_all_flight()

#3.add flight
add_flight(com,name,deptime,arrtime,seat,dep,arr,rd)

#4.add priceinfo
add_price_info(f_id,seat,dis,pri)
#change flight
#delete flight
#search flight
