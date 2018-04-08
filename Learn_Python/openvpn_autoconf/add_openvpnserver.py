#!/usr/sbin/env python
#_*_coding:utf-8_*_
import os

# 生成server配置文件

f = open('server_template').read()
print f.replace('ccd','ccd02')

# 生成密码验证脚本
# 生成密码配置文件
# 生成CCD静态IP路由推送