from flask import flask
import socket 
import psutil 
app = Flask(_name_)

@app.route("/")

def HostName():
	hostname = socket.gethostname()
	ip = socket.gethostbyname(hostname)
	cpus = psutil.cpu_count()
	memory = psutil.virtual_memory()
	
	storage = memory.total >> 30
	return '''{
		hostname: %s
		ip address: %s
		cpus: %s 
		memory: %s GBs}'''
		%(hostname,ip,cpu,storage) 

