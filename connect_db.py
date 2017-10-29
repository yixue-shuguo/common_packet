# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 11:10:39 2017

@author: Administrator
"""

import pymysql 
def mysql(host ,user ,password ,db ,charset ):
    try:
        conn = pymysql.connect(host,user,password ,db, charset)
        return conn
    except Exception as e :
        print ('发生错误'+str(e))
    