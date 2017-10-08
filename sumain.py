#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import src

from src import mailer
from src import seleniumBot

def option_1():
    print ("¿Qué quieres hacer?")
    input = raw_input("1.   Remailing\n"
                      "2.   E-mail anónimo\n"
                      "\n")

    switch = {'1':option_1,
              '2': mailer.amailer,
              99: error
              }
    try:
        switch[input]()
    except KeyError:
        switch[99]()
        option_1()

def option_2():
    print ("¿Qué quieres hacer?")
    input = raw_input("1.   Floodear publicación en FB\n"
                      "2.   ~\n"
                      "\n")

    switch = {'1':seleniumBot.FacebookBot,
              '2': mailer.amailer,
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