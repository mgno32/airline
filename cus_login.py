#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os, sys, string
import MySQLdb
def cus_log_in(cus_email,cus_password):
    global conn_cus
    global cur_cus
    try:
        sql = "select * from airline.customer where customer_email = '%s' and customer_password = '%s'"%(cus_email,cus_password)
        cur_cus.execute(sql)
        result = cur_cus.fetchone()
        print(result)
        return result[0]
    except Exception:
        return 0

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

#if passwd true return true,else return false
def check_passwd(oldpw,cus_id):
	global cur_cus
	global conn_cus
	sql="select * from airline.customer where customer_id = '%s' and customer_password = '%s'"%(cus_id,oldpw)
	cur_cus.execute(sql)
	result=cur_cus.fetchone()
	if result == None:
		return False
	return True
	
#input 2 times new password, if they are the same, change password and return true, else return false.
def change_password(cus_id,new_password,new1_password):
    global cur_cus
    global conn_cus
    if new_password == new1_password:
        result = cur_cus.fetchone()
        sql="update airline.customer set customer_password ='%s' where customer_id='%s'"%(new1_password,cus_id)		
        cur_cus.execute(sql)
        conn_cus.commit()
        return  True
    else:
        return False

def check_email(email):
    global cur_cus
    global conn_cus
    try:
        sql = '''SELECT customer_email FROM airline.customer'''
        cur_cus.execute(sql)
        result = cur_cus.fetchall()
    except Exception :
        return Falsei
    for u in result:
        if u[0] == email:
            return False
    return True


#generate cus_id when a customer sign in
def get_cus_id():
    global cur_cus
    global conn_cus
    try:
        sql = '''SELECT count(customer_id) FROM airline.customer'''
        cur_cus.execute(sql)
        result = cur_cus.fetchone()
        return result[0] + 20000
    except Exception:
        return e

#input email and two times password.
def sign_up(cus_email,new_password,new1_password,sfz,name,tel):
    global cur_cus
    global conn_cus
    if check_email(cus_email)== False: 
        #repeated email
        return 1
    elif new_password != new1_password: 
        #not the same password
        return 2
    else: 
        try:
            cus_id = get_cus_id()
            print(cus_id)
            sql = '''INSERT INTO `airline`.`customer` (`customer_id`, `customer_password`, `customer_email`,`customer_sfz`,`customer_name`,`customer_tel`) VALUES ('%d', '%s', '%s','%s','%s','%s')'''%(cus_id,new_password,cus_email,sfz,name,tel)
            print(sql)
            cur_cus.execute(sql)
            conn_cus.commit()
            #success
            return 3
        except Exception:
            #database error
            return 4


#change sfz
def change_sfz(cus_id,new_sfz):
    global cur_cus
    global conn_cus
    try:
        sql="update airline.customer set customer_sfz ='%s' where customer_id='%s'"%(new_sfz,cus_id)		
        cur_cus.execute(sql)
        conn_cus.commit()
        return  True
    except Exception:
        return False

#change name
def change_name(cus_id,new_name):
    global cur_cus
    global conn_cus
    try:
        sql="update airline.customer set customer_name ='%s' where customer_id='%s'"%(new_name,cus_id)		
        cur_cus.execute(sql)
        conn_cus.commit()
        return  True
    except Exception:
        return False

#change_tel
def change_tel(cus_id,new_tel):
    global cur_cus
    global conn_cus
    try:
        sql="update airline.customer set customer_tel ='%s' where customer_id='%s'"%(new_tel,cus_id)		
        cur_cus.execute(sql)
        conn_cus.commit()
        return  True
    except Exception:
        return False
 

