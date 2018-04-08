#!/sbin/bin/env python
# _*_coding:utf-8_*_
import xml.etree.ElementTree as ET

tree = ET.ElementTree(file='U1TO_A7.xml')
root = tree.getroot()
#for i in root:
 #  print i.tag,i.attrib
#print root[0].tag,root[0].attrib
#print root[0].tag,root[0].text
#for elem in tree.iter(tag='ChildFolder'):
 #  print elem.tag,elem.attrib
for elem in tree.iterfind('ChildFolder'):
    print elem.tag,elem.attrib

