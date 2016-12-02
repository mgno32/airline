#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os, sys, string
import MySQLdb
import cus_login

cus_login.connect()
#1.sign_up
cus_login.sign_up("happygirlzt@gmail.com","123","123","1111111111","ZT","13923332333")

#2.login
cus_id = cus_login.cus_log_in("happygirlzt@gmail.com","125")

#3 change password:
#3.1input old one and check
#3.2input new one, twice
if cus_login.check_passwd("125",cus_id):
    cus_login.change_password(cus_id,"123","123")

#4 change sfz
cus_login.change_sfz(cus_id,"51010000000")

#5 change name
cus_login.change_name(cus_id,"xiaohe")

#6 change tel
cus_login.change_tel(cus_id,"155000000")
