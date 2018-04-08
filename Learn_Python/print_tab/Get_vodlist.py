#/usr/sbin/env python
#_*_coding:utf8_*_
import urllib2
import re
import sys
import base64
import xml.dom.minidom
reload(sys)
sys.setdefaultencoding('utf8')

"""
assetid_list = ['gd_dcdb',{'gd_wgzq':['gd_gqdy','gd_gqsytj','gd_gqjj','gd_gqjs','gd_gqyl','gd_cnxh','gd_wgchd','gd_wgmf','gd_gqty','gd_gqyx','gd_bqyx','gd_bqjj','gd_bqsh','gd_bqyl','gd_bqjs','gd_bqty'],'gd_DOXTV':['gd_DOXTVgqsj','gd_DOXTVmov','gd_DOXTVdsj','gd_DOXTVzy','gd_DOXTVjlp','gd_DOXTVjszy','gd_DOXTVygp'],'gd_thzq':['gd_ztjj','gd_gqyy','gd_gqjc','gd_gqzy','gd_ttyy','gd_bkhc','gd_tthm','gd_ttbk'],'gd_wasunew':['gd_wasudy','gd_wasudsj','gd_wasujl','gd_wasuzy','gd_wasuse','gd_wasukb','gd_wasugq','gd_wasupp']},'gd_yyzq','gd_zxsx2','gd_mfzq']
"""
assetid_list = ['gd_dcdb','gd_DOXTV',{'gd_wgzq':['gd_gqdy','gd_gqsytj','gd_gqjj','gd_gqjs','gd_gqyl','gd_cnxh','gd_wgchd','gd_wgmf','gd_gqty','gd_gqyx','gd_bqyx','gd_bqjj','gd_bqsh','gd_bqyl','gd_bqjs','gd_bqty'],'gd_thzq':['gd_ztjj','gd_gqyy','gd_gqjc','gd_gqzy','gd_ttyy','gd_bkhc','gd_tthm','gd_ttbk'],'gd_wasunew':['gd_wasudy','gd_wasudsj','gd_wasujl','gd_wasuzy','gd_wasuse','gd_wasukb','gd_wasugq','gd_wasupp']},'gd_yyzq','gd_zxsx2','gd_mfzq']


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

file = open("test.text","a+")
for assetid in assetid_list:
    if type(assetid) == dict:
        for dctkey in assetid.keys():
            vodxml = get_vodxml(dctkey)
            get_xmldata(vodxml)
            title_list= '''\n{"title":"%s","assetId":"%s","childContainer"}:[''' %(FF_title,FF_assetId)	
            file.write(title_list)			
            print title_list
            for dctvalues in assetid[dctkey]:
                vodxml = get_vodxml(dctvalues)
                get_xmldata(vodxml)
                print "---------"+dctvalues+"----------"
                for item in itemlist2:
                    assetId = item.getAttribute("assetId")
                    disName = item.getAttribute("displayName")
                    vodlist = '''\n          {"title":"%s","containerId:ObjectID@VODContainer:%s:},''' % (disName,assetId)
                    file.write(vodlist)
                    print vodlist
            print "]}"
            file.write("\n          ]}")
    else:
        vodxml = get_vodxml(assetid)
        get_xmldata(vodxml)
        title_list= '''\n{"title":"%s","assetId":"%s","childContainer"}:[''' %(FF_title,FF_assetId)
        file.write(title_list)
        print title_list
        for item in itemlist2:
            assetId = item.getAttribute("assetId")
            disName = item.getAttribute("displayName")
            vodlist = '''\n            {"title":"%s","containerId:ObjectID@VODContainer:%s:},''' % (disName,assetId)
            file.write(vodlist)
            print vodlist
        print "]}"
        file.write("\n            ]}")
file.close()

"""
assetid = "gd_ztjj"
vodxml = get_vodxml(assetid)
get_xmldata(vodxml)
title_list= '''\n{"title":"%s","assetId":"%s","childContainer"}:[''' %(FF_title,FF_assetId)
print title_list
for item in itemlist2:
    assetId = item.getAttribute("assetId")
    disName = item.getAttribute("displayName")
    vodlist = '''          {"title":"%s","containerId:ObjectID@VODContainer:%s:},''' % (disName,assetId)
    print vodlist
for item in itemlist2:
    assetId = item.getAttribute("assetId")
    disName = item.getAttribute("displayName")
    assetId_en = base64.b64encode(assetId)
    vodlist_en = '''          {"title":"%s","containerId:ObjectID@VODContainer:%s:},''' % (disName,assetId_en)
    print vodlist_en
print(']}')
"""
