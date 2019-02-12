import subprocess 
import time 
import urllib.request
import socket
import sys
import pyfiglet 


ascii_banner = pyfiglet.figlet_format("NetScan")
print(ascii_banner)


def main() : 

	


	r = input("[0]NETWORK SCAN\n" 
		      "[1]IP LOOKUP\n"
		      "[2]RESET(Administrator privileges)\n"
		      "[3]Static arp(Administrator privileges)\n"
		      "[4]MY HOSTNAME \n"
		      "[99]Exit \n"
		      ">: ")
	





	def Network_scanner():	 	 
		t = input("Number of Hosts u wanna Scan ? : ")
		for i in range (1,int(t)):
			address = f"192.168.1.{i}"
			cmd = subprocess.Popen(['ping', "-n", "1", "-w", "200",address],stdout=subprocess.PIPE).wait()
			cmd2 = subprocess.Popen(['arp',"-a",address],stdout=subprocess.PIPE,stderr=subprocess.PIPE).wait()
			if cmd == 0 and cmd2 == 0   :
				ar = subprocess.check_output(['arp' ,'-a', address])
				f = ar.translate(None, b'\r\n').decode().split()
				if address in f :

					print ("HOST ONLINE " + address+ '  MAC ADDRESS==>>> ' +f[10] )
				



	def IP_founder():
		external_ip = urllib.request.urlopen('https://ident.me').read().decode('utf8')
		print("YOUR EXTERNAL IP IS : ",external_ip)
			
	
	def reset():
		r1 = subprocess.Popen(['arp','-d','*'],stdout=subprocess.PIPE,stderr=subprocess.PIPE).wait()
		
		


	def arp_gratuitous():
		ga = subprocess.Popen(['netsh','-c','interface','ipv4','add','neighbors', f'{network_card_name}',f'{ip_address}',f'{mac_address}'],stdout=subprocess.PIPE,stderr=subprocess.PIPE).wait()
		out = subprocess.check_output(["arp","-a",f'{ip_address}'])
		out2=out.translate(None, b'\r\n').decode().split()
		print(ip_address,out2[11])



	def hostname():
		print(socket.gethostname())



#____________________________________________________#

	if r == "0":
		Network_scanner()
		g1=input("[100]Return to the main menu : \n"
				 ":>  " )
		if g1 == "100":
			main()
			
	elif r =="1":
		IP_founder()
		g2=input("[100]Return to the main menu \n:"
				 ":>  " )
		if g2 == "100":
			main()
			 	
	elif r =="2":
		
		reset()	
		g3=input("[100]Return to the main menu :\n"
			     ":>  " )
		if g3 == "100":
			main() 
			
	elif r =="3":
		
		network_card_name = str(input('put your network card name Here : '))
		ip_address = str(input('IP address of the gateway :'))
		mac_address = str(input('MAC ADDRESS of the gateway here :'))
		arp_gratuitous()
		g4=input("[100]Return to the main menu : \n"
			     ":>  " )
		if g4 == "100":
			main() 


	elif r =="4":
		hostname()
		g5=input("[100]Return to the main menu :\n"
				 ":>  " )
		if g5 == "100":
			main() 




	elif r == "99":
		sys.exit()
		
		
if __name__ == "__main__":
	main()		