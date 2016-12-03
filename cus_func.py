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
print(cus_id)
result = cus_os.get_all_orders(cus_id)
print(result)
#2.search flight
#choose departure and arrival and date
result = cus_os.search_flights("2017-01-03","CD","GZ")
print(result)
#3.make_order():
#3.1search flight


#4.
#4.1check all orders
#4.2cancel_order():
#4.2change_order():
#check_order():
