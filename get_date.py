# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 10:55:34 2017

@author: Administrator
"""

import datetime
def getday(n=0):  #
    '''
    获得昨天日期的字符串格式  
    '''
    today=datetime.date.today() 
    nday=datetime.timedelta(days= n) 
    someday=today-nday  
    return someday.strftime("%Y%m%d")


if __name__ == '__main__':
    print (getday())