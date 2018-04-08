#!/usr/bin/env python
# -*- coding:utf-8 -*-
import ssl
from pysphere import VIServer
ssl._create_default_https_context = ssl._create_unverified_context

server = VIServer()
server.connect(IP,user,password)
vmlist = server.get_registered_vms()

vmpathlist = server.get_registered_vms(status='poweredOn')

vm = server.get_vm_by_name("web_public")
vm.get_status()
vm.power_on()
server.connect(IP,user,password)

9.196  9.40
 get_clusters
 get_datacenters
  get_datastores
get_resource_pools