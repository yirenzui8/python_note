#/usr/sbin/env python
import getpass

user = raw_input("please input name:")
passwd = getpass.getpass("passwd:"))
print("username is :%s " %user)
print ("password is %s:" %passwd)