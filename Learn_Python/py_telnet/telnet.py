#/usr/bin/env python
#_*_coding:utf-8_*_
import sys
import os
import telnetlib
def do_telnet(Host,password,finish,commands):
    tn = telnetlib.Telnet(Host,port=23,timeout=10)
    tn.set_debuglevel(2)

    tn.read_until('Password:')
    tn.write(password + '\n')

    tn.read_until(finish)
    #for command in commands:
    #    tn.write('%s\n'%command)
    tn.write(commands + '\n')
    tn.read_until(finish)
    tn.close()

if __name__=='__main__':
    Host = '192.168.5.5'
    password = 'baustem'
    finish = '<H3C>'
    commands ='display cu'
    print type(commands)
do_telnet(Host,password,finish,commands)