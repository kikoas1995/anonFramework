# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
from selenium import webdriver
import os
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import NoSuchElementException
from random import randint, uniform
from abc import ABCMeta, abstractmethod
import names
from src.mailing import TemporaryInbox
from random import randrange
from random import choice
from string import ascii_lowercase, digits

class Bot:

    __metaclass__ = ABCMeta

    def __init__(self, table):
        self.table = table

    @abstractmethod
    def signup(self): pass

    @abstractmethod
    def login(self): pass

    @abstractmethod
    def postsomething(self, text): pass

class PatataBrava(Bot):
    script_dir = os.path.dirname(__file__)
    path = os.path.join(os.path.join(script_dir, os.pardir), '../libraries/geckodriver/geckodriver')
    print path
    driver = webdriver.Firefox(executable_path=path)
    mailer = TemporaryInbox.mailer()

    reg_user = ''.join(choice(ascii_lowercase + digits) for _ in range(10))
    reg_pwd = reg_user
    reg_name = names.get_first_name()
    reg_surname = names.get_last_name()
    reg_mail = mailer.getEmail()
    print ("Tu correo es: " + reg_mail)
    driver.get('http://www.patatabrava.com/reg')
    user = driver.find_element_by_xpath('//*[@id="registeruser"]')
    pwd = driver.find_element_by_xpath('//*[@id="registerpass"]')
    mail = driver.find_element_by_xpath('//*[@id="registeremail"]')
    name = driver.find_element_by_xpath('//*[@id="registernom"]')
    surname = driver.find_element_by_xpath('//*[@id="registercognoms"]')

    user.send_keys(reg_user)
    sleep(randrange(0,3))
    pwd.send_keys(reg_pwd)
    sleep(randrange(0,2))
    mail.send_keys(reg_mail)
    sleep(randrange(0,3))
    name.send_keys(reg_name)
    sleep(randrange(0,3))
    surname.send_keys(reg_surname)
    sleep(randrange(0, 1))
    driver.find_element_by_xpath('//*[@id="registercheck"]').click()
    sleep(randrange(0, 1))
    driver.find_element_by_css_selector('.boton').click()
    sleep(randrange(0, 5))

    # Uni
    driver.find_element_by_css_selector('#universidadsup > option:nth-child(4)').click()
    sleep(randrange(0, 3))
    # Facu
    driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[5]/div[1]/div/div[2]/form/div/div[1]/div[4]/select/option[8]').click()
    sleep(randrange(0, 3))
    # Carrera
    driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[5]/div[1]/div/div[2]/form/div/div[1]/div[5]/select/option[2]').click()
    sleep(randrange(0, 3))
    # Curso
    driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[5]/div[1]/div/div[2]/form/div/div[1]/div[6]/div/select/option[6]').click()
    sleep(randrange(0, 3))
    # Next
    driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[5]/div[1]/div/div[2]/form/div/div[1]/div[7]/input').click()
    sleep(randrange(0, 3))
    # Dia
    driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[5]/div[1]/div/div[2]/form/div/div[1]/div[4]/select[1]/option[2]')
    sleep(randrange(0, 3))
    # Mes
    driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[5]/div[1]/div/div[2]/form/div/div[1]/div[4]/select[2]/option[2]')
    sleep(randrange(0, 3))
    # CP
    driver.find_element_by_xpath('//*[@id="registercp"]').send_keys("28036")
    sleep(randrange(0, 3))
    # Localidad
    driver.find_element_by_xpath('//*[@id="registerpoblacio"]').send_keys("Madrid")
    sleep(randrange(0, 3))
    # Next
    driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[5]/div[1]/div/div[2]/form/div/div[1]/div[10]/input').click()
    sleep(randrange(0, 3))

if __name__ == "__main__":
    patatabrava = PatataBrava('patatabrava')