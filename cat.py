import os,time

logo = """

\033[91m   _____       _______  
\033[91m  / ____|   /\|__   __| 
\033[93m | |       /  \  | |    
\033[93m | |      / /\ \ | |    
\033[92m | |____ / ____ \| |    
\033[92m  \_____/_/    \_\_|    
\033[90m---------------------------------------
Auther : LOST                    
Github : https://github.com/LoSt-SoFtware                     
Yt     : LOST KURDISH 
Tele   : @lo1stt
\033[90m---------------------------------------"""                      
                        
print logo
print ("\033[90m[1]Crack With ID \033[92m(Fb Loging)")
print ("\033[90m[2]Crack With Num\033[91m(No Loging)")
print ("\033[90m[3]About Us")
print ("") 
lost = raw_input ("\033[91mChose:\033[90m ")

if lost =="1":
	print ("\033[92mWait...")
	time.sleep(1)
	os.system("python2 id.py")
elif lost =="2":
	print ("\033[92mWait...")
	time.sleep(1)
	os.system("python2 num.py")
elif lost =="3":
	print ("\033[90m------------------------------")
	print ("\033[91mName : Lost")
	print ("\033[91mAge : 14")
	print ("\033[91mFrom : Kurdistan")
	print ("\033[91mMy User In Social Media : @lo1stt") 
	print ("\033[90m------------------------------")