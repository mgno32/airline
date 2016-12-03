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

#get order id:
def get_ord_id():
    global cur_cus
    global conn_cus
    try:
        sql = '''SELECT count(order_id) FROM airline.orders'''
        cur_cus.execute(sql)
        result = cur_cus.fetchone()
        return result[0] + 400000
    except Exception:
        return e

#get seat numbers:
def get_seat_numbers(flt_id,cus_seat):
    sql = "select seat_num from airline.flight where flight_id = '%d'"%(flt_id)
    cur_cus.execute(sql)
    seat_number_result = cur_cus.fetchone()
    if(cus_seat == 'F'):
        rate = 0.1
    elif(cus_seat == 'Y'):
        rate = 0.2
    elif(cus_seat == 'C'):
        rate = 0.7
    seat_numbers = seat_number_result[0]*rate
    return seat_numbers


#check if seat is available:
def check_seat(flt_id,cus_seat):
    global cur_cus
    global conn_cus
    sql = "SELECT count(order_id) FROM airline.orders where flight_id = '%d' and seat = '%s'"%(flt_id,cus_seat)
    cur_cus.execute(sql)
    result = cur_cus.fetchone()
    if result[0] < get_seat_numbers(flt_id,cus_seat):
        return True
    else:
        return False

#make_ord()
def make_order(cust_id,flt_id,cus_seat,sfz): 
    order_id = get_ord_id()
    global cur_cus
    global conn_cus
    if check_seat(flt_id,cus_seat)== False: 
        #no seat
        return 1
    else: 
        try:
            ord_id = get_ord_id()
            sql = "INSERT INTO `airline`.`orders` (`order_id`, `cus_id`, `flight_id`, `state`, `seat`, `passenger_sfz`) VALUES ('%d', '%d', '%d', '%d', '%s', '%s')"%(ord_id,cust_id,flt_id,2,cus_seat,sfz)
            cur_cus.execute(sql)
            conn_cus.commit()
            #success
            return 2
        except Exception:
            #database error
            return 3


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


#change state
def change_state(ord_id,new_state):
    global conn_cus
    global cur_cus
    try:
        sql = "UPDATE `airline`.`orders` SET `state`='%d' WHERE `order_id`='%s'"%(new_state,ord_id)
        cur_cus.execute(sql)
        conn_cus.commit()
        return 0
    except Exception:
        return 1


#change order
def change_order(cust_id,old_ord_id,new_flt_id):
    try:
        sql = "SELECT seat, passenger_sfz FROM airline.orders where order_id = '%d'"%(old_ord_id)
        cur_cus.execute(sql)
        result = cur_cus.fetchone()
        cus_seat = result[0]
        sfz = result[1]
        make_order(cust_id,new_flt_id,cus_seat,sfz)
    except Exception:
        return 1
    try:
        change_state(old_ord_id,4)
    except Exception:
        conn_cus.rollback()
        return 2


#cancel order
def cancel_order(ord_id):
    change_state(ord_id,3)

#show flights of the same day
def show_flights_to_change(cust_id,old_order_id):
    global cur_cus
    global conn_cus
    try:
        sql = "select flight_id from airline.orders where order_id = '%d'"%(old_order_id)
        cur_cus.execute(sql)
        result = cur_cus.fetchone()
        old_flight_id=result[0]
        sql = "select dept_time, dept, arrv from airline.flight where flight_id = '%d'"%(old_flight_id)
        cur_cus.execute(sql)
        result = cur_cus.fetchone()
        old_dept_time = result[0]
        dep = result[1]
        arr = result[2]
        #search_flights(old_dept_time[0:9],dep,arr)
    except Exception:
        return 1



def disconnect():
    global cur_cus
    global conn_cus
    cur_cus.close()
    conn_cus.close()
