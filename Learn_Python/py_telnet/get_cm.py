#!/usr/bin/env python
#_*_coding:utf-8_*_
import telnetlib
import re
#import threading

def cm_list(host='192.168.9.106'):
    tn=telnetlib.Telnet(host,23,30)
    #tn.set_debuglevel(2)
    tn.read_until('UserName:')
    tn.write('admin'+'\n')
    tn.read_until('Password:')
    tn.write('admin'+'\n')
    tn.read_until('bigwhite>')
    tn.write('enable'+'\n')
    tn.read_until('Password:')
    tn.write('admin'+'\n')
    tn.read_until('bigwhite#')
    tn.write('show cable modem'+'\n')
    tn.write('exit\n')
    return tn.read_all()


def mac_list():
    text=cm_list()
    mac=re.findall(r"[\d,a-f]{4}\.[\d,a-f]{4}\.[\d,a-f]{4}",text)
    ip=re.findall(r"[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[\d]{1,3}",text)
    #print ip,mac
    return mac,ip


def cpe_list(mac,host='192.168.9.106'):
    tn=telnetlib.Telnet(host,23,30)
    #tn.set_debuglevel(2)
    tn.read_until('UserName:')
    tn.write('admin'+'\n')
    tn.read_until('Password:')
    tn.write('admin'+'\n')
    tn.read_until('bigwhite>')
    tn.write('enable'+'\n')
    tn.read_until('Password:')
    tn.write('admin'+'\n')
    tn.read_until('bigwhite#')
    tn.write('show cable modem %s cpe \n' % mac)
    tn.write('exit\n')
    text=tn.read_all()
    mac=re.findall(r"[\d,a-f]{4}\.[\d,a-f]{4}\.[\d,a-f]{4}",text)
    ip=re.findall(r"[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[\d]{1,3}",text)
    #print mac,ip
    return mac,ip



'''
def html_tab(test_html,cpe_ip,cpe_list,i,e):
     a=cpe_ip[e]
     b=cpe_list(i)[0][e]
     #print a,b
     test_html.write("<tr>")
     test_html.write("<td> %s </td>" %(a))
     #print ("\<td\> %s \<\/td\>" % (b))
     test_html.write("<td> %s </td>" %(b))
     test_html.write("</tr>")
'''



def cm_info():
    d=0
    # test_html=open('/var/www/index.html','w')
    test_html=open('d:\PycharmProjects\Learn_Python\index.html','w')
    mac_l=mac_list()
    for i in mac_l[0]:
        cm_ip=mac_l[1][d]
        d=d+1
        cpe_ip=cpe_list(i)[1].append(cm_ip)
        #cpe_ip_l=cpe_ip.insert(0,'cm_ip')
        print cpe_ip,type(cpe_ip),"++++",cm_ip,
        print cpe_ip
        test_html.write('<h4>%s</h4>' % i)
        test_html.write('<table border="1">')
	cpe_l=cpe_list(i)[0]
        for e in range(0,len(cpe_l)):
            print e
           # a=threading.Thread(target=html_tab,args=(test_html,cpe_ip,cpe_list,i,e))
            #a.start()
            a=cpe_ip_l[e]
            b=cpe_l[e]
            #print a,b
            test_html.write("<tr>")
            test_html.write("<td> %s </td>" %(a))
            #print ("\<td\> %s \<\/td\>" % (b))
            test_html.write("<td> %s </td>" %(b))
            test_html.write("</tr>")
            test_html.write("</table>")
            #test_html.write(b)	
    #test_html.write("</table>")
    #test_html.close()

print cm_list('192.168.9.106')