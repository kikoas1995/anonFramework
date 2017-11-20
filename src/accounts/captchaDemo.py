

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

script_dir = os.path.dirname(__file__)

path = os.path.join(os.path.join(script_dir, os.pardir), '../libraries/geckodriver/geckodriver')
driver = webdriver.Firefox(executable_path=path)  # firefox_profile=profile)

driver.get('https://www.google.com/recaptcha/api2/demo')
sleep(5)
driver.find_element_by_css_selector('#recaptcha-demo').click()