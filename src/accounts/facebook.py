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
from selenium.webdriver.support.ui import WebDriverWait

class FaceBook(Bot):

    def signup(self):
        script_dir = os.path.dirname(__file__)
        path = os.path.join(os.path.join(script_dir, os.pardir), '../libraries/geckodriver/geckodriver')
        driver = webdriver.Firefox(executable_path=path)
        tm = TempMail()

        driver.get('https://facebook.com')

        Wait = WebDriverWait(driver, 20)

        Wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='mtm _5wa2 _5dbb']")))
        driver.find_elements_by_css_selector("input[type='radio'][value='1']")[0].click()

        name = driver.find_element_by_name("firstname")
        surname = driver.find_element_by_name("lastname")

        name.send_keys("prueba")
        surname.send_keys("prueba")

        reg_email = driver.find_element_by_name("reg_email__")
        reg_email_confirmation = driver.find_element_by_name("reg_email_confirmation__")
        reg_passwd = driver.find_element_by_name("reg_passwd__")

        reg_email.send_keys("")
        sleep(2)
        reg_email_confirmation.send_keys("")
        reg_passwd.send_keys("")
        sleep(2)

        birthday_day = driver.find_element_by_name("birthday_day")
        birthday_month = driver.find_element_by_name("birthday_month")
        birthday_year = driver.find_element_by_name("birthday_year")

        birthday_day.send_keys('12')
        birthday_month.send_keys('11')
        birthday_year.send_keys('1987')

        return
        print tm.available_domains
        email = tm.get_email_address()
        reg_user = ''.join(choice(ascii_lowercase + digits) for _ in range(10))
        reg_pwd = ''.join(choice(ascii_lowercase + digits) for _ in range(10))
        reg_name = names.get_first_name()
        reg_surname = names.get_last_name()
        reg_mail = email
        print ("Tu correo es: " + reg_mail)

        driver.get('https://www.facebook.com/r.php')
        name = driver.find_element_by_name('firstname')
        surname = driver.find_element_by_name('lastname')
        mail = driver.find_element_by_name('reg_email__')
        mail_confirm =driver.find_element_by_name('reg_email_confirmation__')
        pwd = driver.find_element_by_name('reg_passwd__')

        sleep(randrange(1,5))
        name.send_keys(reg_name)
        sleep(randrange(1,5))
        surname.send_keys(reg_surname)
        sleep(randrange(1,5))
        mail.send_keys(reg_mail)
        sleep(randrange(1,5))
        mail_confirm.send_keys(reg_mail)
        sleep(randrange(1,5))
        pwd.send_keys(reg_pwd)
        sleep(randrange(1,5))
        driver.find_element_by_css_selector('#month > option:nth-child(' + str(randrange(2,11)) +')').click()
        sleep(randrange(1, 5))
        driver.find_element_by_css_selector('#day > option:nth-child(' + str(randrange(2,25)) + ')').click()
        sleep(randrange(1, 5))
        driver.find_element_by_css_selector('#year > option:nth-child(' + str(randrange(28,60)) + ')').click()
        sleep(randrange(1, 5))
        driver.find_element_by_name('sex').click()
        sleep(randrange(1,5))
        driver.find_element_by_name('websubmit').click()
        sleep(randrange(3,5))


        code = self.getConfirmation(email)
        print code

        sleep(randrange(1,5))
        driver.find_element_by_css_selector('#code_in_cliff').send_keys(code)
        sleep(randrange(1,5))
        driver.find_element_by_name('confirm').click()
        #sleep(randrange(3,5))
        #driver.find_element_by_name('submit[Continue]').click()

        print "Pass: " + reg_pwd
        print "Mail: " + email

        pass

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

   facebook = FaceBook()
   facebook.signup()

