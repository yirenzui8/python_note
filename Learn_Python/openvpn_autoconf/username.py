def ser_nu(n):
    for i in range(1,n):
    # userlist = []
    b = 1120 + n
    if n < 10:
        for e in range(1,8):
            userlist.append( "v0" + str(n) + str(b) + "0" + str(e))
    else:
        for e in range(1,8):
            userlist.append ( "v"+ str(n) + str(b) + "0"+str(e))
# return userlist
return userlist,b

ser_nu(22)