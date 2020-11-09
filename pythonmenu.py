import os 
import getpass

os.system("tput setaf 6")
print("Welcome to the All in One Menu")
os.system("tput setaf 2")


print("""
Press 1: For Basic Menu 
Press 2: Hadoop Menu 
Press 3: Docker Menu 
Press 4: Ansible Menu
""")

os.system("tput setaf 4")
choice=input("Enter your choice: ")
print(choice)

if int(choice) == 1:
	os.system("tput setaf 3")
	print("Cool here is your Basic Menu")
	
	
	print("""
	Press 1: To check Date 
	Press 2: To view Calendar
	Press 3: Open firefox
	Press 4: Make directory 
	Press 5: Create a file 
	Press 6: Check status of a user 
	Press 7: Add user 
	Press 8: Add password to the user 
	Press 9: Check memory
	Press 10: Install Hadoop 1.2.1 
	Press 11: Install Docker
	Press 12: Install Ansible
	Press 13: Run tcpdump 
	Press 14: Remote code execution via ssh 
	Press 15: To auto-start programs on Restart
	Press 16: To check the list of ports running
	Press 17: Launch a Apache webserver 
	Press 18: To Exit  
	""")
	print()
	
	while True:
		basic=input("What should i go with: ")
		print(basic)
		
		if int(basic) == 1:
			os.system("date")
		elif int(basic) == 2:
			os.system("cal")
		elif int(basic) == 3:
			os.system("firefox")
		elif int(basic) == 4:
			dir=input("Enter the name of the directory you wish to create: ")
			print(dir)
			mkdir="mkdir"+" "+dir
			os.system("tput setaf 6")
			print("Done")

		elif int(basic) == 5:
			tc=input("Enter the name of file: ")
			ch=input("Enter the desired extension: ")	
			cf=tc+"."+ch
			print(cf)
			touch="touch"+" "+cf
			os.system(touch)

		elif int(basic) == 6:
			os.system("whoami")
		elif int(basic) == 7:
			adusr=input("Enter the name of user you want to add: ")
			user="useradd"+" "+adusr
			os.system(user)
		elif int(basic) == 8:
			usr=input("Which user to set password for: ")
			pswd="passwd"+" "+usr
			os.system(pswd)
		elif int(basic) == 9:
			os.system("free -m")
		elif int(basic) == 10:
			os.system("wget https://archive.apache.org/dist/hadoop/common/hadoop-1.2.1/hadoop-1.2.1-1.x86_64.rpm")
			os.system("rpm -i hadoop-1.2.1-1.x86_64.rpm --force")
		elif int(basic) == 11:
			os.system("touch /etc/yum.repos.d/docker.repo")
			os.chdir("/etc/yum.repos.d/")
			myfile1 = open("docker.repo","w")
			myfile1.write('[docker]\n')
			myfile1.write('baseurl=https://download.docker.com/linux/centos/7/x86_64/stable/\n')
			myfile1.write('gpgcheck=0\n')
			myfile1.close()
			os.system("yum repolist")
			os.system("yum install docker-ce --nobest -y")
			
		elif int(basic) == 12:
			os.system("pip3 install ansible")
		elif int(basic) == 13:
			port=input("Enter the port number: ")
			tcp="tcpdump"+" "+"port"+port
		elif int(basic) == 14:
			ssh=input("Enter the IP address of remote system: ")
			fl=input("Enter the code/file to be executed eg myfile.py: ")
			app=input("Which program would be required to execute the code/file eg python3: ")
			rce="ssh"+" "+ssh+" "+app+" "+fl
		elif int(basic) == 15:
			os.system("tput setaf 1")
			print("Note enter the command or script you want to start whenever you start your O.S")
			os.chdir("/etc/rc.d")
			fd = open("rc.local","a")
			cmd=input("Enter the the command script: ")
			fd.write("\n")
			fd.write(cmd+'\n')
			fd.close()
		elif int(basic) == 16:
			os.system("sudo netstat -tulpn")
		elif int(basic) == 17:
			os.system("yum install httpd")
			os.system("firewall-cmd --permanent --add-service=http")
			os.system("sudo firewall-cmd --permanent --add-service=https")
			os.system("sudo firewall-cmd --reload")
			os.system("systemctl start httpd")
			
			print("Installed and started")
			ww=input("Do you want to create a htmlfile ?: ")
			if ww == "yes":
				nm=input("What should be the name of the file eg-anything.html ")
				print("Ok let me do it")
				os.chdir("/var/www/html")
				newfile = open(nm,"w")
				newfile.write("th3gentleman..Mubin has setup the webserver Just For U enjoy !!")
				newfile.close()
			else:					

				print("No problem as you wish ")

		elif int(basic)==18:
			print("Thankyou for using it regards th3gentleman..MubinGirach")
			break
			


			
			

elif int(choice) == 3:
	os.system("tput setaf 6")
	print("Welcome to the Docker Menu by th3gentleman..MubinGirach ")
	print("Hope you have already installed the Docker")
	os.system("systemctl enable docker")
	os.system("systemctl start docker")
	
	print("""
	Press 19: Firewalls setup 
	Press 20: Pull a container
	Press 21: Starting an existing docker container
	Press 22: Copy anything from host to docker 
	Press 23: Remove an O.S
	Press 24: Run a container
	Press 25: To go to main menu
	Press 0 : To exit
	""")
	
	while True:
		dc=input("What should i do For you ?: ")
		print(dc)
		
		if int(dc) == 19:
			os.system("firewall-cmd --zone=public --add-masquerade --permanent")
			os.system("firewall-cmd --zone=public --add-port=80/tcp --permanent")
			os.system("firewall-cmd --zone=public --add-port=443/tcp --permanent")
			os.system("firewall-cmd --reload")
			os.system("firewall-cmd --list-all")
			os.system("sysetmctl restart docker")
			os.system("systemctl enable docker")
			print("Internet is all yours now :)")
		elif int(dc) == 20:
			cnt=input("Enter the O.S and the version for eg centos:8: ")
			print("Great")
			dockr="docker"+" "+"pull"+" "+cnt
		elif int(dc) == 21:
			os.system("docker ps -a")
			ext=input("Enter the container id: ")
			nme=input("Enter the name: ")
			print("Cool here you go")
			strt="docker"+" "+"start"+" "+ext
			os.system(strt)
			lnch="docker"+" "+"exec"+" "+"-it"+" "+nme+" "+"bash"
			os.system(lnch)
		elif int(dc) == 22:
			py=input("Enter the loaction os source file in host machine: ")
			dst=input("Enter where you want to paste: ")
			container=input("Enter the name of your O.S: ")
			copy="docker cp"+" "+py+" "+container+":"+dst
		elif int(dc) == 23:
			rmv=("Enter the name of O.S: ")
			rm="docker rm -f "+rmv
		elif int(dc) == 24:
			os=input("What should be the name of your O.S: ")
			img=input("Name of image you just pulled: ")
			run="docker run -it"+" "+"--name"+" "+os+" "+img
		elif int(dc) == 25:
			os.system("python3 pythonmenu.py")
		elif int(dc) == 0:
			print("Thanks for using it regards th3gentleman..MubinGirach")
			break
			
		
		else:
			print("Recheck the pressed key")
				
elif int(choice) == 4:
	
	print("Hope your machine has the new Thor called Ansible: ")
	os.system("ansible --version")
	os.system("yum install sshpass")
	print("Let's start")
	
	print("""
	Press 26: For setting up an inventory 
	Press 27: For adding host to your inventory
	Press 28: To copy a file from this machine to all host machine
	Press 29: To go back to main menu 
	Press 30: TO exit 
	""")
	
	while True:
		aq=input("Enter one of the options you would like to choose: ")
		if int(aq) == 26:
			hst=input("Do you have an inventory: ")
			if hst == "yes":
				print("Cool")
			elif hst == "no":
				print("Ok no issues this script is for you")
				os.chdir("/etc/")
				os.system("mkdir ansible")
				os.system("touch /etc/ansible/ansible.cfg")
				os.system("touch /root/ip.txt")
				os.chdir("/etc/ansible")
				fr = open("ansible.cfg","w")
				fr.write('[defaults]\n')
				fr.write('inventory=/root/ip.txt\n')
				fr.write('host_key_checking = False\n')
				fr.close()
			
		elif int(aq) == 27:	
			adhst=input("Do you want to add more host in your inventory?: ")
			if adhst == "yes":
				os.system("cat /etc/ansible/ansible.cfg")
				lcf=input("Enter the location of yout inventory for eg /root/: ")
				filen=input("Name of the file: ")
				ip=input("Enter the ip of the host: ")
				usrname=input("Enter the username: ")
				password=input("Enter the password: ")
				finali=ip+" "+"ansible_user="+usrname+" "+"ansible_ssh_password="+password+" "+"ansible_connection=ssh"
				os.chdir(lcf)
				filew = open(filen,"a")
				filew.write("\n")
				filew.write(ip+" "+"ansible_user="+usrname+" "+"ansible_ssh_password="+password+" "+"ansible_connection=ssh\n")
				filew.close()
			else:
				print("lets continue further")
		elif int(aq) == 28:
			print("Now lets copy a file from this machine to all host machine")
			nos=input("Path of source file from this machine with inverted commas in the start : ")
			nod=input("Path where you want to copy in remote machine(host) ending in inverted commas  : ")
			os.system("cat /etc/ansible/ansible.cfg")
			os.system("\n")
			inevn=input("Enter the inventory path for eg /root/ip.txt: ")
			
			
			copy="ansible all"+" "+"-i"+" "+inevn+" "+"-m copy -a"+" "+" "+"src="+nos+" "+"dest="+nod
			os.system(copy)
		elif int(aq) == 29:
			os.system("python3 pythonmenu.py")
		elif int(aq) == 30:
			print("Thanks for using regards th3gentleman..MubinGirach")
			break
			
elif int(choice)==2:
	print("Hope you have already installed Hadoop")
	os.system("hadoop -version")	
	
	print("""
	Press 31: To start namenode service
	Press 32: To start datanode service 
	Press 33: To either stop namenode or datanode service 
	Press 34: To generate a report
	Press 35: To get back to main menu 
	Press 36: To exit
	""")
	
	while True:
		hdp=input("Enter the desired choice: ")
		if int(hdp) == 31:
			os.system("hadoop-daemon.sh start namenode")
		elif int(hdp) == 32:
			os.system("hadoop-daemon.sh start datanode")
		elif int(hdp) == 33:
			os.system("jps")
			prcsid=input("Enter the process id: ")
			kll="kill "+prcsid
			os.system(kll)
			
		elif int(hdp) == 34:
			os.system("hadoop dfsadmin -report")
		elif int(hdp) == 35:
			os.system("python3 pythonmenu.py")
		elif int(hdp) == 36:
			print("Thanks for using regards th3gentleman..MubinGirach")
			break
		else:
			print("Enter a correct option")
else:
	print("Enter a correct option ..Time is very precious")
	



