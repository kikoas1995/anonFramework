# -*- coding: utf-8 -*-
from selenium import webdriver
import os
from selenium.webdriver.common.keys import Keys
from time import sleep
# hacer este con mechanize lo doy por imposible
class TempAddrMail:

    def __init__(self):
        script_dir = os.path.dirname(__file__)
        path = os.path.join(os.path.join(script_dir, os.pardir), '../libraries/geckodriver/geckodriver')
        self.driver = webdriver.Firefox(executable_path=path)
        self.driver.get('https://temptami.com/')
        sleep(2)

    def getEmailAddr(self,):
        element = self.driver.find_element_by_css_selector('#foo')
        return element.text

    def verify(self, ):
        while(1):
                elements = self.driver.find_elements_by_css_selector(".s")
                if (elements.__len__() > 0):
                    break
                sleep(10)

        str = elements[0].text
        self.driver.close()
        return str.partition(" ")[0]

if __name__ == "__main__":
    m = TempAddrMail()
    s = m.getEmailAddr()
    x = m.verify()

    y = left_text = x.partition(" ")[0]