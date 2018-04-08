#!/usr/sbin/env python
# _*_coding:utf-8_*_
import xml.dom.minidom
dom = xml.dom.minidom.parse('C:\Documents and Settings\Administrator\桌面\ngod_xml\gd_dcdb.xml')
root = dom.documentElement
#print root.nodeName
#print root.nodeValue
#print root.nodeType
itemlist = root.getElementsByTagName('ChildFolder')
print itemlist
for item in itemlist:
    assetId = item.getAttribute("assetId")
    disName = item.getAttribute("displayName")
    print assetId,disName
