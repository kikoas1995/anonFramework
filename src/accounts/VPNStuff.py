import time
import socket
import socks
import urllib2

from stem import Signal
from stem.control import Controller


controller = Controller.from_port(port=9051)
controller.authenticate(password='micontrasenya')

def connectTor():
    socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5 , "127.0.0.1", 9050, True)
    socket.socket = socks.socksocket

def renew_tor():
    controller.signal(Signal.NEWNYM)
    time.sleep(controller.get_newnym_wait())

def showmyip():
    new_ip= urllib2.urlopen("http://icanhazip.com/").read()
    print(new_ip)


for i in range(3):
    renew_tor()
    connectTor()
    showmyip()