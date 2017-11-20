import time
import socket
import socks
import urllib2
import os
from selenium import webdriver
from stem import Signal
from stem.control import Controller

controller = Controller.from_port(port=9051)
controller.authenticate(password='pwd123')

def load_tor():
    socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5 , "127.0.0.1", 9050, True)
    socket.socket = socks.socksocket

def tor_reload():

    controller.signal(Signal.NEWNYM)
    time.sleep(controller.get_newnym_wait())

def getIP():
    script_dir = os.path.dirname(__file__)

    path = os.path.join(os.path.join(script_dir, os.pardir), '../libraries/geckodriver/geckodriver')
    driver = webdriver.Firefox(executable_path=path)  # firefox_profile=profile)
    driver.get('http://icanhazip.com/')
    #new_ip= urllib2.urlopen("http://icanhazip.com/").read()
    #print(new_ip)

for i in range(3):
    tor_reload()
    load_tor()
    getIP()