#/usr/sbin/env python
#_*_coding:UTF-8_*_
import re
import sys
reload(sys)
sys.setdefaultencoding('utf8')

vod_txt=open('3_all.txt').read()
#print vod_txt
#r = re.compile(r"(?<=<\?xml)(.*?)(?<=\<\/FolderContents\>)",re.M)
#r = re.compile(r"(<\?xml).*(\<\/FolderContents\>)$",re.M)
#re=re.compile(r'<\?xml version="1.0" encoding="UTF-8" standalone="yes"\?>(\D*)(.*)\s{1,30}(<(.*)\s{0,50}){0,10}',re.M)
re=re.compile(r'<\?xml version="1.0" encoding="UTF-8" standalone="yes"\?>(\D*)(.*)\s{1,30}(<\FolderContents>)',re.M)
#xml = r.findall(vod_txt,flags=re.DOTALL)
#xml = re.findall(r'(^<\?xml).*(\<\/FolderContents\>)$',vod_txt,flags=re.DOTALL)
#xml = re.match(r'<\?xml>(.*)',vod_txt,flags=re.DOTALL)
xml = re.finditer(vod_txt)

#xmltest = file("xml.text","w+")
#xmltest.write(xml)
#xmltest.close()
for m in xml:
   # xmltest = file("xml.text","a+")
   # xmltest.write(m.group())
  #  xmltest.close()
    print m.group()
