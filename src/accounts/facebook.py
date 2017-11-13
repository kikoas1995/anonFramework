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
from random import randrange
from random import choice
from string import ascii_lowercase, digits
from random import randint
from src.db.cryptodb import *
from Bot import Bot
from tempmail import TempMail
import re
from selenium.webdriver.support.ui import WebDriverWait

class FaceBook(Bot):

    def signup(self):
        script_dir = os.path.dirname(__file__)
        options = webdriver.()


        # options.add_argument("--headless")
        path = os.path.join(os.path.join(script_dir, os.pardir), '../libraries/geckodriver/geckodriver')
        driver = webdriver.Firefox(executable_path=path)
        tm = TemporaryInbox2.TempAddrMail()

        mail = tm.getEmailAddr()
        driver.get('https://facebook.com')

        reg_user = ''.join(choice(ascii_lowercase + digits) for _ in range(10))
        reg_pwd = ''.join(choice(ascii_lowercase + digits) for _ in range(10))
        reg_name = names.get_first_name()
        reg_surname = names.get_last_name()

        Wait = WebDriverWait(driver, 20)

        Wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='mtm _5wa2 _5dbb']")))
        driver.find_elements_by_css_selector("input[type='radio'][value='1']")[0].click()

        name = driver.find_element_by_name("firstname")
        surname = driver.find_element_by_name("lastname")

        name.send_keys(reg_name)
        sleep(randrange(1, 5))
        surname.send_keys(reg_surname)
        sleep(randrange(1, 5))

        reg_email = driver.find_element_by_name("reg_email__")
        reg_email_confirmation = driver.find_element_by_name("reg_email_confirmation__")
        reg_passwd = driver.find_element_by_name("reg_passwd__")

        reg_email.send_keys(mail)
        sleep(randrange(1, 5))
        reg_email_confirmation.send_keys(mail)
        reg_passwd.send_keys(reg_pwd)
        sleep(randrange(1, 5))

        birthday_day = driver.find_element_by_name("birthday_day")
        birthday_month = driver.find_element_by_name("birthday_month")
        birthday_year = driver.find_element_by_name("birthday_year")

        birthday_day.send_keys(randint(1,26))
        sleep(randrange(1, 5))
        birthday_month.send_keys(randint(1,10))
        birthday_year.send_keys(randint(1975,1995))
        sleep(randrange(1, 5))
        websubmit = driver.find_element_by_name("websubmit")
        websubmit.click()
        sleep(randrange(10, 15))
        str = tm.verify()

        driver.find_element_by_css_selector('#code_in_cliff').send_keys(str)
        sleep(randrange(4,6))
        driver.find_element_by_name('confirm').click()

        insert_user("facebook", reg_name, reg_pwd, mail)

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

   facebook = FaceBook()
   facebook.signup()

