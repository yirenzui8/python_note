#/usr/sbin/env python

name=raw_input("Input name please:")
age=int(raw_input("Input age please:"))
job=raw_input("Input job please:")


#print("your name is :%s \nyour age is :%s \nyour job is %s"%(name,age,job))
msg = '''
-------------------
   name:  %s
   age:   %d
   job:   %s
--------end--------
''' %(name,age,job)
print (msg)
