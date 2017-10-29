# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 11:11:11 2017

@author: Administrator
"""

#这是一个发送邮件的模块

import smtplib  
from email.mime.text import MIMEText  
from email.mime.multipart import MIMEMultipart  

#邮箱配置
mail_host="mail.171xue.com"  #服务器  
mail_user="mashuguo@171xue.com"    #用户名  
mail_pass="Ma1987"   #密码  

  
def send_mail(to_list ,cc_list  ,sub,file  ):  
    #to_list：收件人；sub：主题；content：邮件内容  
    me= mail_user  #显示发件人信息 
    msg = MIMEMultipart()  #创建一个带附件的实例  
  
    msg['Subject'] = sub    #设置主题  
    msg['From'] = me  
    msg['To'] = ";".join(to_list)  
    if cc_list is not None:
        msg['Cc'] = ";".join(cc_list)  
    else :
        pass 
    if file is not None:
        att1 = MIMEText(open(file,'rb').read(),'base64','gb2312')  
        att1.add_header('Content-Disposition','attachment', filename = file)  
        msg.attach(att1)  
    else  :
        pass
  
    try:  
        s = smtplib.SMTP()  
        s.connect(mail_host)  #连接smtp服务器  
        s.login(mail_user,mail_pass)  #登陆服务器  
        s.sendmail(me, to_list+cc_list, msg.as_string())  #发送邮件  
        s.close()  
        return True  
    except Exception as  e:  
        print (str(e))
        return False  


if __name__ == '__main__':  
    mailto_list=["mashuguo@171xue.com"]  #发送给谁
    cc_list = ["mashuguo@171xue.com"]
    if send_mail(mailto_list,cc_list ,"这是一个测试邮件","test.xlsx"):  
        print ("发送成功")
    else:  
        print ("发送失败")