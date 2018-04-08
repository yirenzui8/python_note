import hashlib
import MySQLdb
import sys


user_id = sys.argv[1]+"@xmpp.baustem.net"
sha1_user = hashlib.sha1(user_id).hexdigest()
user_pw = sys.argv[2]
print "Add user is %s" % (user_id)
print "Passwd is %s " % (user_pw)
#print "sha1 = %s" % ( hashlib.sha1(user_id).hexdigest())
sql_command = "INSERT INTO tig_users (user_id,sha1_user_id,user_pw) VALUES('%s','%s','%s');" %(user_id,sha1_user,user_pw)
sql_userjid = "INSERT INTO user_jid (jid_sha,jid) VALUES('%s','%s');" %(sha1_user,user_id)
conn = MySQLdb.connect(
    host='120.24.237.83',
    port=3306,
    user='root',
    passwd='TigaseMysqlB4admin',
    db='tigasedb'
   )
cur = conn.cursor()
cur.execute(sql_command)
cur.execute(sql_userjid)
cur.close()
conn.commit()
conn.close()
