#!/usr/local/bin/env python
#_*_*coding:utf8_*_
__author__ = 'Administrator'
import paramiko


ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect("192.168.245.21",22,"root","123456")
#stdin,stdout,stderr = ssh.exec_command("touch testparamiko")
stdin,stdout,stderr = ssh.exec_command("ls -l")
print stdout.readlines()


ssh.close()
