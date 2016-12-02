#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os, sys, string
import MySQLdb
#todo
#log_in()
#change_password
#sign_up

#if wrong password return 0, right password return id
def admin_log_in(admin_email,admin_password):
    global conn_admin
    global cur_admin
    try:
        sql = "select * from airline.administor where administor_email = '%s' and administor_password = '%s'"%(admin_email,admin_password)
        cur_admin.execute(sql)
        result = cur_admin.fetchone()
        return result[0]
    except Exception:
        return 0

#this should be done before any other functions
def connect():
    global conn_admin
    global cur_admin
    try:
        conn_admin = MySQLdb.connect(host='127.0.0.1',user='root',passwd='',db='airline',charset='utf8')
        cur_admin = conn_admin.cursor()
        #print("connect") 
    except Exception:
	    sys.exit()

#if passwd true return true,else return false
def check_passwd(oldpw,admin_id):
	global cur_admin
	global conn_admin
	sql="select * from airline.administor where administor_id = '%s' and administor_password = '%s'"%(admin_id,oldpw)
	cur_admin.execute(sql)
	result=cur_admin.fetchone()
	if result == None:
		return False
	return True
	
#input 2 times new password, if they are the same, change password and return true, else return false.
def change_password(admin_id,new_password,new1_password):
    global cur_admin
    global conn_admin
    if new_password == new1_password:
        result = cur_admin.fetchone()
        sql="update airline.administor set administor_password ='%s' where administor_id='%s'"%(new1_password,admin_id)		
        cur_admin.execute(sql)
        conn_admin.commit()
        return  True
    else:
        return False
