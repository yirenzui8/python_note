#!/usr/sbin/env python
# _*_coding:utf-8_*_
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import xml.dom.minidom
import base64
#vodfile = file('vod_list3.txt',"a+")
#vodfile_en = file("vod_list3_en.txt","a+")
xmlstr = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<FolderContents currentResults="13" totalResults="13" restartAtToken="">
    <FolderFrame folderType="0" displayName="天天百科" assetId="gd_ttbk" parentAssetId="gd_thzq"/>
    <ChildFolder folderAssetId="gd_bnxp" folderType="1" displayName="百年小平" parentAssetId="gd_ttbk" infoText="百年小平" assetId="gd_bnxp">
        <Image rank="1" posterUrl="poster_root/movie_poster/2013/9/4/243x366/16913536.jpg"/>
    </ChildFolder>
    <ChildFolder folderAssetId="gd_30yymhy" folderType="1" displayName="30年银幕记忆" parentAssetId="gd_ttbk" infoText="30年银幕记忆" assetId="gd_30yymhy"/>
    <ChildFolder folderAssetId="gd_60zngqybys" folderType="1" displayName="60周年国庆阅兵仪式" parentAssetId="gd_ttbk" infoText="60周年国庆阅兵仪式" assetId="gd_60zngqybys"/>
    <ChildFolder folderAssetId="gd_kkcz" folderType="1" displayName="库克船长" parentAssetId="gd_ttbk" infoText="库克船长" assetId="gd_kkcz"/>
    <ChildFolder folderAssetId="gd_sgsc" folderType="1" displayName="山高水长" parentAssetId="gd_ttbk" infoText="山高水长" assetId="gd_sgsc"/>
    <ChildFolder folderAssetId="gd_bqxh" folderType="1" displayName="西湖" parentAssetId="gd_ttbk" infoText="西湖" assetId="gd_bqxh"/>
    <ChildFolder folderAssetId="gd_zywzys" folderType="1" displayName="中医五脏养生" parentAssetId="gd_ttbk" infoText="中医五脏养生" assetId="gd_zywzys"/>
    <ChildFolder folderAssetId="gd_dlfgyjzjc" folderType="1" displayName="当卢浮宫遇见紫禁城" parentAssetId="gd_ttbk" infoText="当卢浮宫遇见紫禁城" assetId="gd_dlfgyjzjc"/>
    <ChildFolder folderAssetId="gd_gqbwl" folderType="1" displayName="国情备忘录" parentAssetId="gd_ttbk" infoText="国情备忘录" assetId="gd_gqbwl"/>
    <ChildFolder folderAssetId="gd_bkszs" folderType="1" displayName="孙中山" parentAssetId="gd_ttbk" infoText="孙中山" assetId="gd_bkszs"/>
    <ChildFolder folderAssetId="gd_xzxyj" folderType="1" displayName="玄奘西游记" parentAssetId="gd_ttbk" infoText="玄奘西游记" assetId="gd_xzxyj"/>
    <ChildFolder folderAssetId="gd_wddlc" folderType="1" displayName="伟大的历程" parentAssetId="gd_ttbk" infoText="伟大的历程" assetId="gd_wddlc"/>
    <ChildFolder folderAssetId="gd_ttbktrj" folderType="1" displayName="唐人街" parentAssetId="gd_ttbk" infoText="唐人街" assetId="gd_ttbktrj"/>
</FolderContents>

'''
dom = xml.dom.minidom.parseString(xmlstr)
#dom = xml.dom.minidom.parse('gd_zxsx2.xml')
root = dom.documentElement
itemlist = root.getElementsByTagName('ChildFolder')
item2   = root.getElementsByTagName('FolderFrame')
gd_aId = item2[0].getAttribute("assetId")
gd_Title = item2[0].getAttribute("displayName")
title_list = '''\n{"title":"%s","assetId":"%s","childContainer"}:[ '''% (gd_Title,gd_aId)
#vodfile.write(title_list)
#vodfile_en.write(title_list)
print title_list
for item in itemlist:
    assetId = item.getAttribute("assetId")
    disName = item.getAttribute("displayName")
  #  vodtl = {"title":assetId","containerId:ObjectID@VODContainer:disName:0@ParentId:"}
 #   str(vodtl)
  #  voddct =
    assetId_en = base64.b64encode(assetId)
    #print assetId,disName
   # vodlist = '''\n          {"title":"%s","containerId:ObjectID@VODContainer:%s:0@ParentId:"},''' % (disName,assetId)
  #  vodfile.write(vodlist)
   # print vodlist
    vodlist_en = '''\n        {"title":"%s","containerId:ObjectID@VODContainer:%s:0@ParentId:"},''' % (disName,assetId_en)
  #  vodfile_en.write(vodlist_en)
    print vodlist_en
last = '''\n          ]},'''
#vodfile.write(last)
#vodfile_en.write(last)
#vodfile.close()
print last
