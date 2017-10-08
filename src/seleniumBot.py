# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import NoSuchElementException
from random import randint, uniform


def FacebookBot():
    driver = webdriver.Firefox(executable_path='/etc/geckodriver/geckodriver')

    login_email = "kikoas1995@gmail.com"
    login_pass = "nintendo.95"

    driver.get('https://www.facebook.com/login.php?login_attempt=1&lwv=110')
    print("Página de log-in de FB")

    email = driver.find_element_by_xpath("//*[@id='email']")
    pwd = driver.find_element_by_xpath("//*[@id='pass']")
    button = driver.find_element_by_xpath("//*[@id='loginbutton']")

    email.send_keys(login_email)
    sleep(1)
    pwd.send_keys(login_pass)
    sleep(1.5)
    button.click()

    post_text = driver.find_element_by_xpath("//*[@id='u_0_1f']/div/div[2]/textarea")
    post_button = driver.find_element_by_xpath("//*[@id='u_0_1e']/div[3]/div/div[2]/div/button")

    x = 0
    while x < 10:
        post_text.send_keys(randint)
        sleep(uniform(0.3, 4.76))
        post_button.click()
        x+=1

if __name__ == "__main__":
    FacebookBot()