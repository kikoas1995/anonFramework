#!/usr/bin/python
# -*- coding: utf-8 -*-

from src.mailing import TemporaryInbox, mailer
from src.accounts import osoigo

def option_1():
    print ("¿Qué quieres hacer?")
    input = raw_input("1.   Remailing (Mixmaster) \n"
                      "2.   E-mail anónimo (Anonymouse) \n"
                      "3.   Bandeja de entrada temporal (Tempail) \n"
                      "\n")

    switch = {'1':option_1, # LINKEAR CON MIXMASTER!!
              '2': mailer.amailer,
              '3': TemporaryInbox.tempMail,
              99: error
              }
    try:
        switch[input]()
    except KeyError:
        switch[99]()
        option_1()

def option_2():
    print ("¿Qué quieres hacer?")
    input = raw_input("1.   Registrar usuario en Osoigo.com\n"
                      "2.   Loguearte en Osoigo(registra al menos a un usario antes!)\n"
                      "3.   Spam de Support\n")

    switch = {'1': osoigo.osoigo.signup(),
              '2': osoigo.osoigo.login(),
              '3': osoigo.osoigo.supportAll(),
              99: error
              }
    try:
        switch[input]()
    except KeyError:
        switch[99]()
        option_2()

def error():
    print("La opción seleccionada no está disponible. Selecciona un valor de entre los siguientes")


def init():
    input = raw_input("1.   Mailing\n"
                      "2.   Scripts en Selenium\n"
                      "3.   ~~~~~~\n"
                      "\n")
    switch = {'1':option_1,
              '2': option_2,
              '99': error
              }
    try:
        switch[input]()
    except KeyError:
        switch[99]()
        init()

def main():

    print ("Bienvenido al FrameWork.\n"
           "Aquí están las opciones disponibles:\n")

    init()



if __name__ == "__main__":
    main()