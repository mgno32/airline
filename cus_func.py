#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os, sys, string
import MySQLdb
import cus_os
import cus_login
cus_login.connect()
cus_os.connect()
#1.check all orders of a customer
cus_id = cus_login.cus_log_in("happygirlzt@gmail.com","123")
result = cus_os.get_all_orders(cus_id)

#2.search flight
#choose departure and arrival and date
result = cus_os.search_flights("2017-01-03","CD","GZ")

#3.make a order
#3.1search flight
result = cus_os.make_order(20000,30000,'F','1234020')
print(result)

#4.change flights
#4.1 todo: show flights of the same day
#r =  cus_os.show_flights_to_change(20000,400001)
#4.2 change order
cus_os.change_order(20000,400001,30002)
#4.3 cancel order
cus_os.cancel_order(400001)


