
# -*- coding: utf-8 -*-
from selenium import webdriver
import os
from time import sleep
import names
from src.mailing import TemporaryInbox2
from random import randrange,randint
from random import choice
from string import ascii_lowercase, digits
from src.db.cryptodb import *
from Bot import Bot
import re

class SceneBeta(Bot):

    def signup(self):
        script_dir = os.path.dirname(__file__)
        regex = 'Contraseña = .*" '

        path = os.path.join(os.path.join(script_dir, os.pardir), '../libraries/geckodriver/geckodriver')
        driver = webdriver.Firefox(executable_path=path)#firefox_profile=profile)

        tm = TemporaryInbox2.TempAddrMail()
        email = tm.getEmailAddr()

        reg_user = names.get_last_name().lower() + str(randint(50,150)) + names.get_first_name().lower()
        if reg_user.__len__() > 12:
            reg_user = reg_user[:11]

        reg_pwd = ''.join(choice(ascii_lowercase + digits) for _ in range(10))
        reg_mail = email
        print ("Tu correo es: " + reg_mail)

        driver.get('http://www.scenebeta.com/user/register')
        sleep(3)
        mail = driver.find_element_by_name('mail')
        user = driver.find_element_by_name('name')

        sleep(randrange(1, 3))
        user.send_keys(reg_user)
        sleep(randrange(1, 3))
        mail.send_keys(reg_mail)
        sleep(randrange(1,3))
        driver.find_element_by_name('legal_accept').click()
        res = driver.find_element_by_class_name('field-prefix').text
        x = eval(res.replace('=', ''))
        driver.find_element_by_name('captcha_response').send_keys(x)
        sleep(randrange(1, 3))
        driver.find_element_by_id('edit-submit').click()
        sleep(randrange(1, 3))


        pwd = self.getPass(tm)
        insert_user("scenebeta", reg_user, pwd, reg_mail)


        driver.close()

        return

    def login(self):
        script_dir = os.path.dirname(__file__)
        path = os.path.join(os.path.join(script_dir, os.pardir), '../libraries/geckodriver/geckodriver')
        driver = webdriver.Firefox(executable_path=path)
        random_user = get_random_user("scenebeta")
        driver.get('http://www.scenebeta.com/user/login?destination=comment%2Freply%2F26123%23comment-form')
        sleep(3)
        user = driver.find_element_by_name('name')
        pwd = driver.find_element_by_name('pass')

        reg_user = random_user[1]
        reg_pwd = random_user[2]

        user.send_keys(reg_user)
        sleep(randrange(1, 3))
        pwd.send_keys(reg_pwd)
        sleep(randrange(1, 3))
        buttons = driver.find_elements_by_id('edit-submit')
        if (buttons.__len__() > 1):
            buttons[1].click()
        else:
            buttons[0].click()
        return driver

    def getPass(self, tm):

        while True:
            try:
                tm.driver.find_element_by_css_selector('.f').click()
                break
            except:
                sleep(10)

        tm.driver.switch_to_default_content()
        frame = tm.driver.find_element_by_id("idIframe")
        tm.driver.switch_to_frame(frame)
        smth = tm.driver.find_element_by_xpath('/html/body')
        txt = smth.text
        title_search = re.search('a: (.*)', txt, re.IGNORECASE)
        title = title_search.group(1)

        tm.driver.close()

        return title

    def comment(self):

        driver = self.login()
        print("Selecciona el foro donde deseas postear:")
        print("1. PSP\n2. NDS\n3. WII\n4. Apple\n5. Android\n6. PC\n7. PS3\n")
        sel = 0
        input = ''
        while (sel < 1 or sel > 7):
            input = raw_input("> ")
            sel = int(input)
        switch = {'1': 'http://psp.scenebeta.com/',
                  '2': 'http://nds.scenebeta.com/',
                  '3': 'http://wii.scenebeta.com/',
                  '4': 'http://iapps.scenebeta.com/',
                  '5': 'http://android.scenebeta.com/',
                  '6': 'http://www.scenebeta.com/',
                  '7': 'http://ps3.scenebeta.com/',
                  }

        url = switch[input]

        driver.get(url)

        print("\nSelecciona una noticia para comentar:\n")
        nodes = driver.find_elements_by_class_name('node')
        i=0
        for node in nodes:
            elem = node.find_element_by_css_selector('h2:nth-child(1) > a:nth-child(1)')
            print (str(i+1) + '. ' + elem.text)
            i+=1
        sel = 0
        while (sel < 1 or sel > nodes.__len__()):
            sel = raw_input("> ")
            sel = int(sel)
        nodes[sel-1].find_element_by_css_selector('h2:nth-child(1) > a:nth-child(1)').click()
        sleep(randrange(2,4))
        driver.find_element_by_css_selector('.comment_add > a:nth-child(1)').click()
        sleep(randrange(1,3))
        print("\nIntroduce asunto:\n")
        asunto = raw_input('> ')
        print("\nIntroduce cuerpo del mensaje:\n")
        msg = raw_input('> ')
        driver.find_element_by_name('subject').send_keys(asunto)
        driver.find_element_by_css_selector('#wysiwyg-toggle-edit-comment').click()
        sleep(1)
        driver.find_element_by_css_selector('#edit-comment').send_keys(msg)

        driver.find_element_by_css_selector('#edit-submit').click()


if __name__ == "__main__":

    sb = SceneBeta()
    sb.signup()
    sb.comment()

