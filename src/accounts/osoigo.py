
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


class Osoigo(Bot):

    def signup(self):
        script_dir = os.path.dirname(__file__)
        path = os.path.join(os.path.join(script_dir, os.pardir), '../libraries/geckodriver/geckodriver')
        driver = webdriver.Firefox(executable_path=path)

        tm = TempMail()
        email = tm.get_email_address()

        reg_user = ''.join(choice(ascii_lowercase + digits) for _ in range(10))
        reg_pwd = ''.join(choice(ascii_lowercase + digits) for _ in range(10))
        reg_name = names.get_first_name()
        reg_surname = names.get_last_name()
        reg_mail = email
        print ("Tu correo es: " + reg_mail)

        driver.get('https://www.osoigo.com/es/login.html?action=register')
        sleep(randrange(1,3))
        #driver.find_element_by_class_name("inicar_sesion nuevo no-margin-r selected").click()
        sleep(randrange(1,3))

        mail = driver.find_element_by_name('email')
        name = driver.find_element_by_name('first_name')
        surname = driver.find_element_by_name('last_name')
        #user = driver.find_element_by_name('username')
        pwd = driver.find_element_by_name('password')
        driver.find_element_by_name('terms_of_use').click()
        button = driver.find_element_by_class_name("boton_login")

        sleep(randrange(1,2))
        name.send_keys(reg_name)
        sleep(randrange(1,2))
        surname.send_keys(reg_surname)
        sleep(randrange(1,2))
        mail.send_keys(reg_mail)
        sleep(randrange(1,2))
        pwd.send_keys(reg_pwd)
        sleep(randrange(1,2))
        button.click()
        sleep(randrange(1,2))

        insert_user("osoigo", reg_name, reg_pwd, reg_mail)

        return

    def login(self):
        script_dir = os.path.dirname(__file__)
        path = os.path.join(os.path.join(script_dir, os.pardir), '../libraries/geckodriver/geckodriver')
        driver = webdriver.Firefox(executable_path=path)
        random_user = get_random_user("osoigo")
        driver.get('https://www.osoigo.com/es/login.html')

        reg_pwd = random_user[2]
        reg_mail = random_user[3]

        driver.find_element_by_name('email').send_keys(reg_mail)
        sleep(randrange(1, 3))
        driver.find_element_by_name('password').send_keys(reg_pwd)
        sleep(randrange(1, 3))
        driver.find_element_by_class_name('boton_login').click()
        sleep(randrange(1, 3))

        return driver

    def supportAll(self):

        driver = self.login()
        driver.get('https://www.osoigo.com/es/preguntas.html')

        apoyos = driver.find_elements_by_class_name('apoyar1')
        print apoyos.__len__()
        for boton in apoyos:

                boton.click()
                sleep(randrange(1,3))
                driver.find_element_by_name('facebook').click()
                sleep(randrange(1,2))
                driver.find_element_by_xpath('/html/body/div[6]/div/article[3]/section/div/article/section[2]/form/div/a').click()
                sleep(randrange(2, 4))
                driver.get('https://www.osoigo.com/es/preguntas.html')
                sleep(randrange(2, 4))
                continue


if __name__ == "__main__":

    osoigo = Osoigo()
    osoigo.signup()
    osoigo.supportAll()