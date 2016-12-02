#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os, sys, string
import MySQLdb
import administor_login

administor_login.connect()

#login
admin_id = administor_login.admin_log_in("123@126.com","123")

#1 change password:
#1.1input old one and check
#1.2input new one, twice
if administor_login.check_passwd("123",admin_id):
    print(administor_login.change_password(admin_id,"125","125"))


