#!/usr/bin/env python
# -*- coding:utf-8 -*-

import ssl
from pysphere import VIServer
ssl._create_default_https_context = ssl._create_unverified_context

server = VIServer()
server.connect("192.168.5.30","root","12345678")
vmlist = ['[Data1] file forward 1.60/file forward 1.60.vmx','[Data1] drupa_test_nginx_1.15/drupa_test_nginx_1.15.vmx', '[Data1] druapl_test_web/druapl_test_web.vmx', '[Data1] drupal_test_web_1.17/drupal_test_web_1.17.vmx', '[Data1] drupal_test_mysql_1.18/drupal_test_mysql_1.18.vmx', '[Data1] win 2008 1.62w/win 2008 1.62w.vmx', '[Data1] win 2008 1.61w/win 2008 1.61w.vmx']
for vm_name in vmlist:
    vm = server.get_vm_by_path(vm_name)
    vm.power_on()

server.connect("192.168.5.31","root","12345678")
vmlist = ['[datastore1 (4)] to Nagra-5.251/to Nagra-5.251.vmx']
vm = server.get_vm_by_path('[datastore1 (4)] to Nagra-5.251/to Nagra-5.251.vmx')
vm.power_on()

server.connect("192.168.5.32","root","12345678")
vmlist = ['[datastore1 (6)] 5.143bianyi server/5.143bianyi server.vmx', '[datastore1 (6)] linuxAS5.5/linuxAS5.5.vmx', '[datastore1 (6)] linuxas5.5 --9.176/linuxas5.5 --9.176.vmx', '[datastore1 (6)] linuxAS5.5--5.169/linuxAS5.5--5.169.vmx']
for vm_name in vmlist:
    vm = server.get_vm_by_path(vm_name)
    vm.power_on()

server.connect("192.168.5.33","root","12345678")
vmlist = ['[datastore1 (18)] SVN ubuntu13.10-5.146/SVN ubuntu13.10-5.146.vmx]']
for vm_name in vmlist:
    vm = server.get_vm_by_path(vm_name)
    vm.power_on()

server.connect("192.168.5.35","root","12345678")
vmlist = ['[datastore1 (2)] Incognito Acs-5.134/Incognito Acs-5.134.vmx']
for vm_name in vmlist:
    vm = server.get_vm_by_path(vm_name)
    vm.power_on()

server.connect("192.168.5.36","root","12345678")
vmlist = ['[datastore1 (2)] Incognito Acs-5.134/Incognito Acs-5.134.vmx']
for vm_name in vmlist:
    vm = server.get_vm_by_path(vm_name)
    vm.power_on()
	
server.connect("192.168.5.37","root","12345678")
vmlist = ['[datastore1 (21)] puma ubuntu 10.04 5.147/puma ubuntu 10.04 5.147.vmx', '[datastore1 (21)] redhat5.5-5.131/redhat5.5-5.131.vmx']
for vm_name in vmlist:
    vm = server.get_vm_by_path(vm_name)
    vm.power_on()
	

server.connect("192.168.5.38","root","12345678")
vmlist = ['[datastore1 (10)] XMTP_5.102/XMTP_5.102.vmx', '[datastore1 (10)] OpenIms/OpenIms.vmx', '[datastore1 (10)] '[datastore1 (10)] OpenAcs 5.76/OpenAcs 5.76.vmx', '[datastore1 (10)] PPPoe_Centos_5.116/PPPoe_Centos_5.116.vmx', '[datastore1 (10)] Ddns_210.76.110.110/Ddns_210.76.110.110.vmx', '[datastore1 (10)] winxp/winxp.vmx','[datastore1 (10)] Bcc_5.105/Bcc_dengtao-5.121.vmx', '[datastore1 (10)] debian_DNS_110.50/debian_DNS_110.50.vmx', '[datastore1 (10)] Debian_PCSCF_210.76.110.51/Debian_PCSCF_210.76.110.51.vmx', '[datastore1 (10)] Debian_ICSCF_210.76.110.52/Debian_ICSCF_210.76.110.52.vmx', '[datastore1 (10)] Debian_SCSCF_210.76.110.53/Debian_SCSCF_210.76.110.53.vmx', '[datastore1 (10)] Debian_HSS_210.76.110.54_1/Debian_HSS_210.76.110.54.vmx']
for vm_name in vmlist:
    vm = server.get_vm_by_path(vm_name)
    vm.power_on()

server.connect("192.168.5.39","root","12345678")
vmlist = ['[datastore1 (8)] DMS-Server 5.101/xp 5.101.vmx','[datastore1 (3)] PPPoe_Server_ipv6_5.118/PPPoe_Server_ipv6_5.118.vmx']
for vm_name in vmlist:
    vm = server.get_vm_by_path(vm_name)
    vm.power_on()

server.connect("192.168.5.40","root","12345678")
vmlist = ['[datastore1 (17)] mailserver 5.22/mailserver.vmx', '[datastore1 (17)] redmine ubuntu12.04-5.141/redmine ubuntu12.04-5.141.vmx', '[datastore1 (17)] SIP server 5.185/SIP server 5.185.vmx', '[datastore1 (17)] web server 253.212/web server 253.212.vmx', '[datastore1 (17)] NGOD-redhat 5.180/linux 6.0.vmx', '[datastore1 (17)] NFS TFTP 5.65/DM Server.vmx', '[datastore1 (17)] openacs server 5.66/Red Hat Enterprise Linux 5.vmx', '[datastore1 (17)] bcc-cs 5.62/bcc-cs1.vmx']
for vm_name in vmlist:
    vm = server.get_vm_by_path(vm_name)
    vm.power_on()

server.connect("192.168.5.41","root","12345678")
vmlist = ['[datastore1 (20)] acs-5.29/acs-5.29.vmx', '[datastore1 (20)] webtest 1.31/webtest 1.31.vmx', '[datastore1 (20)] redhat 5.4 5.182/redhat 5.4 5.182.vmx', '[datastore1 (20)] lvs-test-1.23/lvs-test-1.23.vmx', '[datastore1 (20)] lvs-test-1.24/lvs-test-1.24.vmx', '[datastore1 (20)] yum-repo_5.253/yum-repo_5.28.vmx', '[datastore1 (20)] Tigase-5.102/Tigase-5.102.vmx', '[datastore1 (20)] lvs-test-1.21/lvs-test-1.21.vmx', '[datastore1 (20)] lvs-test-1.22/lvs-test-1.22.vmx', '[datastore1 (20)] Mysql-server-5.153/Mysql-server-5.153.vmx']
for vm_name in vmlist:
    vm = server.get_vm_by_path(vm_name)
    vm.power_on()

server.connect("192.168.5.42","root","12345678")
vmlist = ['[data169] redhat AS6.0 192.168.5.181/redhat AS6.0 192.168.5.181.vmx', '[data169] DLNA server/DLNA server.vmx', '[data169] puma-int 5.176/puma-int 5.176.vmx', '[data169] svn bakcup13.10 5.177/svn bakcup13.10 5.177.vmx']
for vm_name in vmlist:
    vm = server.get_vm_by_path(vm_name)
    vm.power_on()

server.connect("192.168.5.43","root","12345678")
vmlist = ['[datastore1] to Nagra/to Nagra.vmx', '[datastore1] forward-nagralog/forward-nagralog.vmx']
for vm_name in vmlist:
    vm = server.get_vm_by_path(vm_name)
    vm.power_on()
	
server.connect("192.168.5.44","root","12345678")
vmlist = ['[datastore1 (1)] Bcc_dengtao-5.121/Bcc_dengtao-5.121.vmx', '[datastore1 (1)] FTP-server-5.125/FTP-server-5.125.vmx', '[datastore1 (1)] DNS-dengtao-11.22/DNS-dengtao-11.22.vmx', '[datastore1 (1)] Ubuntu 64 \xe4\xbd\x8d/Ubuntu 64 \xe4\xbd\x8d.vmx']
for vm_name in vmlist:
    vm = server.get_vm_by_path(vm_name)
    vm.power_on()
	
server.connect("192.168.5.45","root","12345678")
vmlist = ['[datastore44] 192.168.10.192/192.168.10.192.vmx','[datastore44] ubuntu_64bit-5.137/ubuntu_64bit-5.137.vmx', '[datastore44] Mysql-Server-5.154_ha/Mysql-Server-5.154_ha.vmx']
for vm_name in vmlist:
    vm = server.get_vm_by_path(vm_name)
    vm.power_on()



	
server.disconnect()
EsxiList = {'192.168.5.30':['[Data1] file forward 1.60/file forward 1.60.vmx','[Data1] drupa_test_nginx_1.15/drupa_test_nginx_1.15.vmx', '[Data1] druapl_test_web/druapl_test_web.vmx', '[Data1] drupal_test_web_1.17/drupal_test_web_1.17.vmx', '[Data1] drupal_test_mysql_1.18/drupal_test_mysql_1.18.vmx', '[Data1] win 2008 1.62w/win 2008 1.62w.vmx', '[Data1] win 2008 1.61w/win 2008 1.61w.vmx'],'192.168.5.31':['[datastore1 (4)] to Nagra-5.251/to Nagra-5.251.vmx'],'192.168.5.32':['[datastore1 (6)] 5.143bianyi server/5.143bianyi server.vmx', '[datastore1 (6)] linuxAS5.5/linuxAS5.5.vmx', '[datastore1 (6)] linuxas5.5 --9.176/linuxas5.5 --9.176.vmx', '[datastore1 (6)] linuxAS5.5--5.169/linuxAS5.5--5.169.vmx'],'192.168.5.33':['[datastore1 (18)] SVN ubuntu13.10-5.146/SVN ubuntu13.10-5.146.vmx'],'192.168.5.35':['[datastore1 (2)] Incognito Acs-5.134/Incognito Acs-5.134.vmx'],'192.168.5.36':['[datastore1 (21)] puma ubuntu 10.04 5.147/puma ubuntu 10.04 5.147.vmx', '[datastore1 (21)] redhat5.5-5.131/redhat5.5-5.131.vmx'],'192.168.5.37':['[datastore1 (19)] Incognito-ACS_5.138-/Incognito-ACS_5.138-.vmx', '[datastore1 (19)] Syslog_server_5.117/Syslog_server_5.117.vmx','[datastore1 (19)] openacs-5.149/openacs-5.149.vmx'],'192.168.5.38':['[datastore1 (10)] XMTP_5.102/XMTP_5.102.vmx', '[datastore1 (10)] OpenIms/OpenIms.vmx','[datastore1 (10)] OpenAcs 5.76/OpenAcs 5.76.vmx', '[datastore1 (10)] PPPoe_Centos_5.116/PPPoe_Centos_5.116.vmx', '[datastore1 (10)] Ddns_210.76.110.110/Ddns_210.76.110.110.vmx', '[datastore1 (10)] winxp/winxp.vmx','[datastore1 (10)] Bcc_5.105/Bcc_dengtao-5.121.vmx', '[datastore1 (10)] debian_DNS_110.50/debian_DNS_110.50.vmx', '[datastore1 (10)] Debian_PCSCF_210.76.110.51/Debian_PCSCF_210.76.110.51.vmx', '[datastore1 (10)] Debian_ICSCF_210.76.110.52/Debian_ICSCF_210.76.110.52.vmx', '[datastore1 (10)] Debian_SCSCF_210.76.110.53/Debian_SCSCF_210.76.110.53.vmx', '[datastore1 (10)] Debian_HSS_210.76.110.54_1/Debian_HSS_210.76.110.54.vmx'],'192.168.5.39':['[datastore1 (8)] DMS-Server 5.101/xp 5.101.vmx','[datastore1 (3)] PPPoe_Server_ipv6_5.118/PPPoe_Server_ipv6_5.118.vmx'],'192.168.5.40':['[datastore1 (17)] mailserver 5.22/mailserver.vmx', '[datastore1 (17)] redmine ubuntu12.04-5.141/redmine ubuntu12.04-5.141.vmx', '[datastore1 (17)] SIP server 5.185/SIP server 5.185.vmx', '[datastore1 (17)] web server 253.212/web server 253.212.vmx', '[datastore1 (17)] NGOD-redhat 5.180/linux 6.0.vmx', '[datastore1 (17)] NFS TFTP 5.65/DM Server.vmx', '[datastore1 (17)] openacs server 5.66/Red Hat Enterprise Linux 5.vmx', '[datastore1 (17)] bcc-cs 5.62/bcc-cs1.vmx'],'192.168.5.41':['[datastore1 (20)] acs-5.29/acs-5.29.vmx', '[datastore1 (20)] webtest 1.31/webtest 1.31.vmx', '[datastore1 (20)] redhat 5.4 5.182/redhat 5.4 5.182.vmx', '[datastore1 (20)] lvs-test-1.23/lvs-test-1.23.vmx', '[datastore1 (20)] lvs-test-1.24/lvs-test-1.24.vmx', '[datastore1 (20)] yum-repo_5.253/yum-repo_5.28.vmx', '[datastore1 (20)] Tigase-5.102/Tigase-5.102.vmx', '[datastore1 (20)] lvs-test-1.21/lvs-test-1.21.vmx', '[datastore1 (20)] lvs-test-1.22/lvs-test-1.22.vmx', '[datastore1 (20)] Mysql-server-5.153/Mysql-server-5.153.vmx'],'192.168.5.42':['[data169] redhat AS6.0 192.168.5.181/redhat AS6.0 192.168.5.181.vmx', '[data169] DLNA server/DLNA server.vmx', '[data169] puma-int 5.176/puma-int 5.176.vmx', '[data169] svn bakcup13.10 5.177/svn bakcup13.10 5.177.vmx'],'192.168.5.43':['[datastore1] to Nagra/to Nagra.vmx', '[datastore1] forward-nagralog/forward-nagralog.vmx'],'192.168.5.44':['[datastore1 (1)] Bcc_dengtao-5.121/Bcc_dengtao-5.121.vmx', '[datastore1 (1)] FTP-server-5.125/FTP-server-5.125.vmx', '[datastore1 (1)] DNS-dengtao-11.22/DNS-dengtao-11.22.vmx', '[datastore1 (1)] Ubuntu 64 \xe4\xbd\x8d/Ubuntu 64 \xe4\xbd\x8d.vmx'],'192.168.5.45':['[datastore44] 192.168.10.192/192.168.10.192.vmx','[datastore44] ubuntu_64bit-5.137/ubuntu_64bit-5.137.vmx', '[datastore44] Mysql-Server-5.154_ha/Mysql-Server-5.154_ha.vmx']}
