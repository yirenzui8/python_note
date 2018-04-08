__author__ = 'Administrator'
#!/usr/local/bin/env python
#_*_conding:utf8_*_
import paramiko

t = paramiko.Transport(("192.168.1.21",22))
t.connect(username="root",password="123456")
sftp = paramiko.SFTPClient.from_transport(t)
remotepath = '/tmp/test.txt'
localpath = 'D:/test.txt'
sftp.get(remotepath,localpath)
t.close()