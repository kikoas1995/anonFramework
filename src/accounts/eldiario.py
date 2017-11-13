
# -*- coding: utf-8 -*-
from selenium import webdriver
import os
from time import sleep
import names
from random import randrange
from random import randint
from random import choice
from string import ascii_lowercase, digits
from src.db.cryptodb import *
from Bot import Bot
from src.mailing import TemporaryInbox
import re


class Eldiario(Bot):

    def signup(self):
        script_dir = os.path.dirname(__file__)
        path = os.path.join(os.path.join(script_dir, os.pardir), '../libraries/geckodriver/geckodriver')
        driver = webdriver.Firefox(executable_path=path)
        regex = 'http:\/\/www.eldiario.es\/usuarios\/confirmacion-alta\/.*l"'


        mailer = TemporaryInbox.mailer()
        reg_mail = mailer.getEmail()

        reg_user = ''.join(choice(ascii_lowercase + digits) for _ in range(10))
        reg_pwd = ''.join(choice(ascii_lowercase + digits) for _ in range(10))
        reg_name = names.get_first_name()
        reg_surname = names.get_last_name()
        print ("Tu correo es: " + reg_mail)

        driver.get('https://seguro.eldiario.es/usuarios/registro.html')
        sleep(randrange(1,3))

        mail = driver.find_element_by_name('email')
        name = driver.find_element_by_name('name')
        surname = driver.find_element_by_name('surname')
        user = driver.find_element_by_name('nick')
        city = driver.find_element_by_css_selector('#ediProvince > option:nth-child(' + str(randint(1,54)) + ')')
        pwd = driver.find_element_by_name('password')
        pwd2 = driver.find_element_by_name('repeatpassword')

        element = driver.find_element_by_css_selector('.lightbox-trigger')
        driver.execute_script("""
        var element = arguments[0];
        element.parentNode.removeChild(element);
        """, element)
        sleep(1)
        driver.find_element_by_css_selector('.frm-lightbox > label:nth-child(3)').click()

        button = driver.find_element_by_css_selector("#edi-signup-register")

        sleep(1)
        user.send_keys(reg_user)
        sleep(1)
        mail.send_keys(reg_mail)
        sleep(1)
        pwd.send_keys(reg_pwd)
        sleep(1)
        pwd2.send_keys(reg_pwd)
        sleep(1)
        name.send_keys(reg_name)
        sleep(1)
        surname.send_keys(reg_surname)
        sleep(1)
        city.click()
        sleep(1)
        button.click()
        sleep(1)
        try:
            while (button.is_displayed()):
                button.click()
        except:
            sleep(randrange(1,3))

        verification = TemporaryInbox.linkVerification(mailer, regex)
        verification = verification[:-1]
        driver.get(verification)

        insert_user("eldiario", reg_name, reg_pwd, reg_mail)

        driver.close()

        return

    def login(self):
        script_dir = os.path.dirname(__file__)
        path = os.path.join(os.path.join(script_dir, os.pardir), '../libraries/geckodriver/geckodriver')
        driver = webdriver.Firefox(executable_path=path)
        random_user = get_random_user("eldiario")
        driver.get('https://seguro.eldiario.es/usuarios/login.html')

        reg_pwd = random_user[2]
        reg_mail = random_user[3]

        driver.find_element_by_name('email').send_keys(reg_mail)
        driver.find_element_by_name('password').send_keys(reg_pwd)
        driver.find_element_by_css_selector('label.frm-label:nth-child(2) > span:nth-child(1)').click()
        driver.find_element_by_id('edi-login-submit').click()

        return driver

    def comment(self):

        driver = self.login()
        elements = []
        sleep(2)
        elements.append(driver.find_element_by_css_selector('div.rg-main:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > article:nth-child(1) > h2:nth-child(2) > strong:nth-child(1) > a:nth-child(1)'))
        elements.append(driver.find_element_by_css_selector('div.row:nth-child(1) > div:nth-child(1) > article:nth-child(1) > div:nth-child(2) > h2:nth-child(1) > a:nth-child(1)'))
        elements.append(driver.find_element_by_css_selector('h2.typ-3:nth-child(3) > a:nth-child(1)'))

        print "Selecciona una noticia de entre las siguientes para comentar(ordenadas de más reciente a más antigua en portada):"
        print "1: " + elements[0].get_attribute("title")
        print "2: " + elements[1].get_attribute("title")
        print "3: " + elements[2].get_attribute("title")

        sel = -1
        while ((sel > 4) or (sel < 1)):
            sel = input("> ")

        try:
            driver.set_page_load_timeout(5)
            elements[int(sel) - 1].click()
        except Exception:
            sleep(1)
        textarea = driver.find_element_by_css_selector('#edi_comment-text')
        msg = raw_input('Introduce tu mensaje:')
        textarea.send_keys(msg)
        driver.find_element_by_css_selector('#edi-comment-button').click()
        print "Mensaje enviado!"



if __name__ == "__main__":

    eldiario = Eldiario()
    eldiario.signup()
    #eldiario.login()
    eldiario.comment()