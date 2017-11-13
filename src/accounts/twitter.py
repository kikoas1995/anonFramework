
# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
from selenium import webdriver
import os
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from abc import ABCMeta, abstractmethod
import names
from src.mailing import TemporaryInbox
from random import randrange
from random import choice
from string import ascii_lowercase, digits
from src.db.cryptodb import *
from Bot import Bot
from tempmail import TempMail
import re


class Instagram(Bot):

    def signup(self):
        script_dir = os.path.dirname(__file__)
        path = os.path.join(os.path.join(script_dir, os.pardir), '../libraries/geckodriver/geckodriver')
        driver = webdriver.Firefox(executable_path=path)

        tm = TempMail()
        email = tm.get_email_address()

        reg_user = ''.join(choice(ascii_lowercase + digits) for _ in range(10))
        reg_pwd = ''.join(choice(ascii_lowercase + digits) for _ in range(10))
        reg_name = names.get_full_name()
        reg_mail = email
        print ("Tu correo es: " + reg_mail)

        driver.get('https://mobile.twitter.com/signup?type=email')
        sleep(5)
        name = driver.find_element_by_id('oauth_signup_client_fullname')
        mail = driver.find_element_by_name('oauth_signup_client_phone_number')

        sleep(randrange(1,2))
        name.send_keys(reg_name)
        sleep(randrange(1,2))
        mail.send_keys(reg_mail)
        sleep(randrange(1,2))
        driver.find_element_by_name('commit')
        sleep(randrange(1,4))

        pwd = driver.find_element_by_id('password')

        pwd.send_keys(reg_pwd)
        sleep(randrange(1,2))

        return

    def login(self):
        script_dir = os.path.dirname(__file__)
        path = os.path.join(os.path.join(script_dir, os.pardir), '../libraries/geckodriver/geckodriver')
        driver = webdriver.Firefox(executable_path=path)
        random_user = get_random_user("patatabrava")
        driver.get('http://m.patatabrava.com/es/login/')



    def postsomething(self, text):
        print "Esta página no permite postear nada sin confirmación. :("
        pass

    def getConfirmation(self, email):

        tm = TempMail()
        # print email
        while (1):
            box = tm.get_mailbox(email)  # list of emails
            if type(box) is dict:
                # print "Waiting for mails"
                sleep(10)
            elif type(box) is list:
                # print box[0]['mail_text']
                m = re.findall('\n\d+\n', box[0]['mail_text'])
                return m[0][1:-1]



if __name__ == "__main__":

    instagram = Instagram()
    instagram.signup()
