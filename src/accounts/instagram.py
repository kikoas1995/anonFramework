
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
from src.mailing import TemporaryInbox2
from random import randrange,randint
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

        tm = TemporaryInbox2.TempAddrMail()
        email = tm.getEmailAddr()

        reg_user = names.get_last_name().lower() + str(randint(50,150)) + names.get_first_name().lower()
        if reg_user.__len__() > 12:
            reg_user = reg_user[:11]

        reg_pwd = ''.join(choice(ascii_lowercase + digits) for _ in range(10))
        reg_name = names.get_full_name()
        reg_mail = email
        print ("Tu correo es: " + reg_mail)

        driver.get('https://www.instagram.com/accounts/emailsignup/')
        sleep(5)
        mail = driver.find_element_by_name('emailOrPhone')
        name = driver.find_element_by_name('fullName')
        user = driver.find_element_by_name('username')
        pwd = driver.find_element_by_name('password')
        button = driver.find_elements_by_tag_name("button")[1]

        sleep(randrange(1,3))
        name.send_keys(reg_name)
        sleep(randrange(1,3))
        user.send_keys(reg_user)
        sleep(randrange(1,3))
        mail.send_keys(reg_mail)
        sleep(randrange(1,3))
        pwd.send_keys(reg_pwd)
        sleep(randrange(1,3))

        len = 1
        while (len > 0):
            try:
                button.click()
                sleep(randrange(1,5))
                e = driver.find_elements_by_xpath("//*[contains(text(), 'Sorry, ')]")
                len = e.__len__()
                if (len > 0):
                    user.clear()
                    sleep(randrange(1, 3))
                    user.send_keys(reg_user + ''.join(choice(ascii_lowercase + digits) for _ in range(3)))
            except:
                break

        elements = driver.find_elements_by_xpath("//*[contains(text(), 'Skip')]")

        for element in elements:
            try:
                element.click()
                sleep(randrange(3,6))
            except:
                continue

        insert_user("instagram", reg_user, reg_pwd, reg_mail)

        return

    def login(self):
        script_dir = os.path.dirname(__file__)
        path = os.path.join(os.path.join(script_dir, os.pardir), '../libraries/geckodriver/geckodriver')
        driver = webdriver.Firefox(executable_path=path)
        random_user = get_random_user("instagram")
        driver.get('https://www.instagram.com/accounts/login/?hl=es')
        sleep(3)
        user = driver.find_element_by_name('username')
        pwd = driver.find_element_by_name('password')

        reg_user = random_user[3]
        reg_pwd = random_user[2]

        user.send_keys(reg_user)
        sleep(randrange(1, 3))
        pwd.send_keys(reg_pwd)
        sleep(randrange(1, 3))

        elements = driver.find_elements_by_xpath("//*[contains(text(), 'Iniciar ')]")

        for ele in elements:
            if ele.is_displayed():
                ele.click()
                sleep(randrange(3,5))

        return driver

    def stalk(self, user):

        driver = self.login()
        driver.get('https://www.instagram.com/' + user)

        elements = driver.find_elements_by_xpath("//*[contains(text(), 'Follow')]")

        driver.get('https://www.instagram.com/')




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
    #instagram.signup()
    instagram.stalk("angelillama")