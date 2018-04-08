#/usr/bin/env python
import re
text = open("bndservice.log",'r').read()
print text

#pattern = re.compile(r'{"sgname":"javax\.xml\.ws","displayname":".{30,38}","sgicon":\w+,"category":\w+,"desc":\w+,"version":"\d\.\d\.\d\.\w\d{12}","status":"\w+"}')
#match = pattern.search(text)
#print match.group()