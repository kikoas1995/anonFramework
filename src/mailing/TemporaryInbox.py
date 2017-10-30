# -*- coding: utf-8 -*-
import time
import requests
from lxml import html
import re

class mailer:
    def mailBox(self,):
        result = self.newsEmails(self.email,self.oturum,self.tarih,self.cookies)
        if not result:
            return False
        else:
            return result

    def newTarih(self,):
        url = 'https://tempail.com/'
        r = requests.get(url,cookies=self.cookies)
        tree = html.fromstring(r.content)
        self.tarih = tree.xpath('//*[@id="epostalar"]/script[1]/text()')[0].split('"')[1]

    def getEmail(self,):
        url = 'https://tempail.com/'
        r = requests.get(url)
        self.cookies = r.cookies
        tree = html.fromstring(r.content)
        email = tree.xpath('//*[@id="eposta_adres"]/@value')
        variables = tree.xpath('/html/head/script/text()')
        if email:
            self.email = email[0]
            if variables:
                for variable in variables[0].split('\n'):
                    variable = variable.strip()
                    if 'oturum' in variable:
                        self.oturum = variable.split('"')[1]

                    if 'tarih' in variable:
                        self.tarih = variable.split('"')[1]
        return self.email

    def newsEmails(self,email,oturum,tarih,cookies):
        url = 'https://tempail.com/en/api/kontrol/'
        data = {'email':email,'oturum':oturum,'tarih':tarih,'geri_don':'https://tempail.com/en/'}
        r = requests.post(url,data=data,cookies=cookies)

        if r.status_code != 200:
            return False
        else:
            self.newTarih()
            mail = dict()
            tree = html.fromstring(r.content)
            mail['Sender']= tree.xpath('/html/body/ul/li[2]/a/div[2]/text()')[0]
            mail['Subject']= tree.xpath('/html/body/ul/li[2]/a/div[3]/text()')[0]
            email_content_url = tree.xpath('/html/body/ul/li[2]/a/@href')[0]
            r = requests.get(email_content_url,cookies=cookies)
            tree = html.fromstring(r.content)
            url_body = tree.xpath('//*[@id="iframe"]/@src')[0]
            r = requests.get(url_body,cookies=cookies)
            mail['body'] = r.content
            return mail

def tempMail():
    m = mailer()
    email_address = m.getEmail()
    print 'Correo volátil: %s' % email_address
    while True:
        result = m.mailBox()
        if result:
            print result['body']
            #print result
        time.sleep(5)

def linkVerification(m, regex):
    #print 'Correo volátil: %s' % email_address
    while True:
        result = m.mailBox()
        if result:
            try:
                m = re.search(regex, result['body']).group(0)
                return m
            except AttributeError:
                print "No se encontró el link de confirmación."
            #print result
        time.sleep(5)

if __name__ == "__main__":
    linkVerification(mailer(), '')