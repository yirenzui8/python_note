#!/usr/bin/env python

import paramiko
import threading
import os

iplist = {'192.168.5.24':"b4admin",'192.168.5.27':"b4admin",'192.168.5.30':"12345678",'192.168.5.31':"12345678",'192.168.5.32':"12345678",'192.168.5.33': "12345678",'192.168.5.35':"12345678",'192.168.5.36':"12345678",'192.168.5.37':"12345678",'192.168.5.38':"12345678",'192.168.5.39':"12345678",'192.168.5.40':"12345678",'192.168.5.41':"12345678",'192.168.5.42':"12345678",'192.168.5.43':"12345678",'192.168.5.44':"12345678",'192.168.5.45':"12345678",'192.168.5.145':"123456"}
# iplist = {'192.168.5.24':"b4admin",'192.168.5.27':"b4admin",'192.168.5.30':"12345678",'192.168.5.32':"12345678",'192.168.5.33': "12345678",'192.168.5.35':"12345678",'192.168.5.36':"12345678",'192.168.5.38':"12345678",'192.168.5.41':"12345678",'192.168.5.42':"12345678",'192.168.5.43':"12345678",'192.168.5.44':"12345678",'192.168.5.45':"12345678",'192.168.5.142':"BcM3330",'192.168.5.145':"123456"}

def ssh2(ip,username,passwd,cmd):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip,22,username,passwd,timeout=5)
    stdin,stdout,stderr = ssh.exec_command(cmd)
    print "server_IP %s shutdowning.... "% ip
    print stdout.readlines()
    ssh.close()

for ip in iplist.keys():
	username = "root"
	passwd = iplist[ip]
	threads = []
	cmd = "halt"
	ping_ip = os.system('ping -n 4 %s >>nul' % ip)
	if ping_ip == 0:
	    ssh2(ip,username,passwd,cmd)
	    a = threading.Thread(target=ssh2,args=(ip,username,passwd,cmd))
	    a.start()
	else:
	    print "server_ip %s is down" % ip
		
