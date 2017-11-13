# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
from selenium import webdriver
import os
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
import names
from src.mailing import TemporaryInbox
from random import randrange
from random import choice
from string import ascii_lowercase, digits
from src.db.cryptodb import *
from Bot import Bot


class PatataBrava(Bot):

    def signup(self):
        script_dir = os.path.dirname(__file__)
        path = os.path.join(os.path.join(script_dir, os.pardir), '../libraries/geckodriver/geckodriver')
        driver = webdriver.Firefox(executable_path=path)
        mailer = TemporaryInbox.mailer()
        regex = 'http:\/\/www.patatabrava.com\/\?uid.*" '
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
        sleep(randrange(1,3))
        pwd.send_keys(reg_pwd)
        sleep(randrange(1,2))
        mail.send_keys(reg_mail)
        sleep(randrange(1,3))
        name.send_keys(reg_name)
        sleep(randrange(1,3))
        surname.send_keys(reg_surname)
        sleep(randrange(1, 2))
        driver.find_element_by_xpath('//*[@id="registercheck"]').click()
        sleep( randrange(7, 10))
        driver.find_element_by_css_selector('.registre-bloque > div:nth-child(2)').click()
        wait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.boton'))).click()

        sleep(randrange(5, 8))

        # Uni
        wait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#universidadsup > option:nth-child(4)'))).click()
        sleep(randrange(3, 6))
        # Facu
        wait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#facultadsup > option:nth-child(6)'))).click()
        sleep(randrange(1, 3))
        # Carrera
        wait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#carrerasup > option:nth-child(2)'))).click()
        sleep(randrange(1, 3))
        # Curso
        wait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#curssup > option:nth-child(2)'))).click()
        sleep(randrange(2, 3))
        # Next
        wait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.boton'))).click()
        sleep(randrange(3, 5))

        # CP
        wait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#registercp'))).send_keys("28036")
        sleep(randrange(1, 3))
        # Localidad
        wait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#registerpoblacio'))).send_keys("Madrid")
        sleep(randrange(7, 10))
        # Next
        wait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.boton'))).click()
        sleep(randrange(3, 4))

        verification = TemporaryInbox.linkVerification(mailer, regex)
        verification = verification[:-1]
        sleep(randrange(12, 15))
        driver.get(verification)

        # User
        driver.find_element_by_xpath('//*[@id="login2"]').send_keys(reg_mail)
        sleep(randrange(2, 3))
        # Pwd
        driver.find_element_by_xpath('//*[@id="pass2"]').send_keys(reg_pwd)
        sleep(randrange(4, 5))
        # Click
        wait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input.stepButton'))).click()
        sleep(randrange(4, 6))

        # Registro realizado, insertamos el usuario en la DB encriptada
        insert_user("patatabrava", reg_user, reg_pwd, reg_mail)
        driver.close()

        pass

    def login(self):
        script_dir = os.path.dirname(__file__)
        path = os.path.join(os.path.join(script_dir, os.pardir), '../libraries/geckodriver/geckodriver')
        driver = webdriver.Firefox(executable_path=path)
        random_user = get_random_user("patatabrava")
        driver.get('http://m.patatabrava.com/es/login/')

        driver.find_element_by_css_selector('#login-username').send_keys(random_user[1])
        sleep(randrange(1, 5))
        driver.find_element_by_css_selector('#login-password').send_keys(random_user[2])
        sleep(randrange(4, 5))
        wait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.btn'))).click()

    def postsomething(self, text):
        print "Esta página no permite postear nada sin confirmación. :("
        pass




if __name__ == "__main__":
    patatabrava = PatataBrava()
    patatabrava.signup()
    patatabrava.login()