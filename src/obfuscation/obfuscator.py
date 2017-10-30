# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import os
from time import sleep


def lang_obfuscator(text):

    script_dir = os.path.dirname(__file__)
    path = os.path.join(os.path.join(script_dir, os.pardir), '../libraries/geckodriver/geckodriver')
    driver = webdriver.Firefox(executable_path=path)
    driver.get('https://skaillz.net/obfuscator/')
    driver.find_element_by_id('user-text').clear()
    driver.find_element_by_id('user-text').send_keys(text)
    driver.find_element_by_id('obfuscate-button').click()

    wait = WebDriverWait(driver, 10)
    confirm = wait.until(EC.element_to_be_clickable((By.ID, "result")))
    ret = confirm.text
    driver.close()
    return ret

if __name__ == "__main__":
    lang_obfuscator("Example")