#!/usr/sbin/env python
#-*-coding:utf-8-*-
import urllib2
import re
import sys
import base64
import xml.dom.minidom
reload(sys)
sys.setdefaultencoding('utf8')

list = ['gd_dcdb','gd_wgzq','gd_DOXTV','gd_thzq','gd_wasunew','gd_yyzq','gd_zxsx2','gd_mfzq']
def get_vodxml(assetid):
    cookies = urllib2.HTTPCookieProcessor()
    opener = urllib2.build_opener(cookies)
    xml_request = '''<?xml version="1.0" encoding="UTF-8"?><GetFolderContents portalId="1" client="8230002127347814" assetId="%s" account="7563017" languageCode="zh-CN" includeFolderProperties="Y" includeSubFolder="Y" includeSelectableItem="Y" startAt="1" depth="1" maxItems="200" profile="A25"></GetFolderContents>'''% (assetid)
    url = "http://192.168.1.202:8085/GetFolderContents"
    request = urllib2.Request(
        url     = url,
        headers = {'Content-Type' : 'application/xml','charset':'UTF-8'},
        data    = xml_request)
    f=opener.open(request)
    dirlist = f.read()
    xml = re.sub(r'\s+<\?xml','<?xml',dirlist)
    return xml

def get_xmldata(vodxml): 
    dom = xml.dom.minidom.parseString(vodxml)
    root = dom.documentElement
    global FF_assetId,FF_title,itemlist2
    itemlist1= root.getElementsByTagName('FolderFrame')
    itemlist2 = root.getElementsByTagName('ChildFolder')
    FF_assetId = itemlist1[0].getAttribute("assetId")
    FF_title = itemlist1[0].getAttribute("displayName")
    return FF_assetId,FF_title,itemlist2


for i in list:
    vodxml = get_vodxml(i)
    get_xmldata(vodxml)
    title_list= '''\n{"title":"%s","assetId":"%s","childContainer"}:[''' %(FF_title,FF_assetId)
    print title_list
    for item in itemlist2:
        assetId = item.getAttribute("assetId")
        disName = item.getAttribute("displayName")
        gpAssetId = item.getAttribute("parentAssetId")
        fType = item.getAttribute("folderType")
        while fType == 0 :
            vodxml = get_vodxml(assetId)
            get_xmldata(vodxml)
            assetId = item.getAttribute("assetId")
            disName = item.getAttribute("displayName")
            pAssetId = item.getAttribute("parentAssetId")
            fType = item.getAttribute("folderType")
            vodlist = '''"##FT:"%s"##GPAID:"%s"##PAID:"%s"##AID:"%s''' %(fType,pAssetId,gpAssetId,assetId)
            print vodlist
        vodlist = '''"##FT:"%s"##GPAID:"%s"##PAID:"%s"##AID:"%s''' %(fType,gpAssetId,gpAssetId,assetId)
        print vodlist
    print ("\n   ]}")