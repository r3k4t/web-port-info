import os
import sys


os.system('clear')


print ("                     ====================================")
print ("                     |          Web Port Info           |")
print ("                     ====================================")
print ("                     | Author : Rahat Khan Tusar(rkt)   |")
print ("                     | Github : https://github.com/r3k4t|")
print ("                     ====================================")


from nmap import nmap
ip   = raw_input('Enter a ip address  :')
port =     input('Enter a port number :')
nmap=nmap.PortScanner()
nmap.scan(ip,'21-443')
nmap.command_line()
nmap.scaninfo()
nmap.all_hosts()
nmap[ip].hostname()
nmap[ip].state()
nmap[ip].all_protocols()
nmap[ip]['tcp'].keys()
print (nmap[ip].tcp(port))
