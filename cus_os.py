#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os, sys, string
import MySQLdb

#todo
#this should be done before any other functions
def connect():
    global conn_cus
    global cur_cus
    try:
        conn_cus = MySQLdb.connect(host='127.0.0.1',user='root',passwd='',db='airline',charset='utf8')
        cur_cus = conn_cus.cursor()
        #print("connect") 
    except Exception:
	    sys.exit()

#get_ord_id()

#make_ord(

#check_ord()
def get_all_orders(cus_id):
    global conn_cus
    global cur_cus
    try:
        sql = "select * from airline.orders where cus_id = '%s'"%(cus_id)
        cur_cus.execute(sql)
        result = cur_cus.fetchall()
        return result
    except Exception:
        return 0

#change_ord()

#cancel_ord()
#search()
def search_flights(dep_date,dep,arr):
    global conn_cus
    global cur_cus
    try:
        sql = "SELECT * FROM airline.flight where date(dept_time) = '%s' and dept = '%s'and arrv = '%s'"%(dep_date,dep,arr)
        cur_cus.execute(sql)
        result = cur_cus.fetchall()
        if result[0]!=None:
            return result
        else:
            return 0 #not any flight
    except Exception:
        return 1 #database error

def disconnect():
    global cur_cus
    global conn_cus
    cur_cus.close()
    conn_cus.close()
