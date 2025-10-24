#!/bin/python
from flask import Flask, jsonify
import socket, time
app = Flask(__name__)
hosts = ["google.com", "jesus.net",]
def ping(h):
	try:
		s = socket.create_connection((h,80),1);
		s.close()
		return True
	except:
		return False
		
@app.get("/status")
def status():
	return jsonify({h:ping(h) for h in hosts})
app.run(port=5001)
