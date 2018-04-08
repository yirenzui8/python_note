#!/usr/bin/env python
#_*_coding:utf:8_*_
import MySQLdb
import sys
import json

 # user_id = sys.argv[1]+""
 # user_pw = sys.argv[2]



# Generate instert SQL
def sql_cmd(nu):
    def ser_nu(n):
    # for i in range(1,n):
        userlist = []
        b = 1120 + n
        if n < 10:
            for e in range(1,8):
                userlist.append( "v0" + str(n) + str(b) + "0" + str(e))
        else:
            for e in range(1,8):
                userlist.append ( "v"+ str(n) + str(b) + "0"+str(e))
    # return userlist
        return userlist,b
    port = ser_nu(nu)[1]
    vpnusername = ser_nu(nu)[0]
    RaOssCfg = '''"RaOssCfg": {
            "VpnSever": {
                "server": "120.24.237.83",
                "port": "%s",
                "proto": "udp"
            },
            "RaIms2VpnSever": {
                "proxy": "sip:sip.baustem.net",
                "route": "sip:120.25.90.139:5060",
                "expiry": "1800",
                "bandwidth": "512"
            }
        }''' %(port)
    RaServerCfg = '''"RaServerCfg": {
            "Vpn": {
                "username":"%s",
                "password":"%s"
            },
            "Ims2Vpn": {
                "authUsername":"%s",
                "authPassword":"%s"
            }
              }'''%(vpnusername[0],vpnusername[0],vpnusername[0],vpnusername[0])
    RaClientCfg = '''"RaClientCfg": {
            "VpnAccountList": [
                {
                    "username": "%s",
                    "password": "%s"
                },
                {
                    "username": "%s",
                    "password": "%s"
                },{
                    "username": "%s",
                    "password": "%s"
                },
                {
                    "username": "%s",
                    "password": "%s"
                },
                {
                    "username": "%s",
                    "password": "%s"
                },
                {
                    "username": "%s",
                    "password": "%s"
                }
            ],
            "ImsAccountList": [
                {
                    "username": "%s",
                    "password": "%s"
                },
                {
                    "username": "%s",
                    "password": "%s"
                },{
                    "username": "%s",
                    "password": "%s"
                },
                {
                    "username": "%s",
                    "password": "%s"
                },
                {
                    "username": "%s",
                    "password": "%s"
                },
                {
                    "username": "%s",
                    "password": "%s"
                }
            ]
        }'''%(vpnusername[1],vpnusername[1],vpnusername[2],vpnusername[2],vpnusername[3],vpnusername[3],vpnusername[4],vpnusername[4],vpnusername[5],vpnusername[5],vpnusername[6],vpnusername[6],vpnusername[1],vpnusername[1],vpnusername[2],vpnusername[2],vpnusername[3],vpnusername[3],vpnusername[4],vpnusername[4],vpnusername[5],vpnusername[5],vpnusername[6],vpnusername[6])
    sql_cmd = '''insert into t_cfg (function,RaOssCfg,RaServerCfg,RaClientCfg) VALUES('GetRaAccountInfo','%s','%s','%s');'''%(RaOssCfg,RaServerCfg,RaClientCfg)
    return sql_cmd
#print "sha1 = %s" % ( hashlib.sha1(user_id).hexdigest())

def mysql_con(nu):
    conn = MySQLdb.connect(
        host='123.57.77.248',
        port=3306,
        user='root',
        passwd='TomcatMysqlB4admin',
        db='baustem'
       )
    cur = conn.cursor()
    cur.execute(sql_cmd(nu))
    cur.close()
    conn.commit()
    conn.close()
for nu in range():
    print("add server %s"%(nu))
    mysql_con(nu)
# mysql_con(nu)
