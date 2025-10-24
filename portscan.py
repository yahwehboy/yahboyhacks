#!/bin/python
import socket
target = input("Enter targer IP address: ")
start_port = int(input("Enter the start port number: "))
end_port = int(input("Enter the end port number: "))

for port in range(start_port, end_port + 1):
	try:
		s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.settimeout(1)
		s.connect((target, port))
		print(f"Port {port} is open")
		s.close()
	except:
		pass
