#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os, sys, string
import MySQLdb
#this should be done before any other functions
def connect():
    global conn_admin
    global cur_admin
    try:
        conn_admin = MySQLdb.connect(host='127.0.0.1',user='root',passwd='',db='airline',charset='utf8')
        cur_admin = conn_cus.cursor()
        #print("connect") 
    except Exception:
	    sys.exit()

#get price id:
def get_price_id():
    global cur_admin
    global conn_admin
    try:
        sql = '''SELECT count(price_id) FROM airline.price_info'''
        result = cur_admin.fetchone()
        return result[0] + 100000
    except Exception:
        return 1

#get flight id:
def get_flight_id():
    global cur_admin
    global conn_admin
    try:
        sql = '''SELECT count(flight_id) FROM airline.flight'''
        result = cur_admin.fetchone()
        return result[0] + 30000
    except Exception:
        return 1

def show_all_price_info():
    global cur_admin
    global conn_admin
    try:
        sql = "SELECT * FROM airline.price_info"
        cur_admin.execute(sql)
        result = cur_admin.fetchall()
        return 0
    except Exception:
        return 1
   
def show_all_flight():
    global cur_admin
    global conn_admin
    try:
        sql = "SELECT * FROM airline.flight"
        cur_admin.execute(sql)
        result = cur_admin.fetchall()
        return 0
    except Exception:
        return 1

def add_flight(com,name,deptime,arrtime,seat,dep,arr,rd):
    try:
        f_id = get_flight_id()
        sql = "INSERT INTO `airline`.`flight` (`flight_id`, `company`, `flight_name`, `dept_time`, `arrv_time`, `seat_num`, `dept`, `arrv`, `real_dept_time`) VALUES ('%d', '%s, '%s', '%s', '%s', '%d', '%s', '%s', '%s')"%(f_id,com,name,deptime,arrtime,seat,dep,arr,rd)
        cur_admin.execute(sql)
        conn_admin.commit()
        return 0
    except Exception:
        return 1


def add_price_info(f_id,seat,dis,pri):
    try:
        p_id = get_price_id()
        sql = "INSERT INTO `airline`.`price_info` (`price_id`, `flight_id`, `seat_lable`, `discount`, `original_price`) VALUES ('%d', '%d', '%d', '%d', '%d');"%(p_id,f_id,seat,dis,pri)
        cur_admin.execute(sql)
        conn_admin.commit()
        return 0
    except Exception:
        return 1


def change_price_info(p_id,choice):

    return 0

def change_flight(f_id,choice):
    return 0

def disconnect():
    global cur_cus
    global conn_cus
    cur_cus.close()
    conn_cus.close()
