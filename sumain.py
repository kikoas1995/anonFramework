#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
sys.path.insert(0, 'src')
from mailer import anonMailer

def option_1():
    print ("¿Qué quieres hacer?")
    input = raw_input("1.   Remailing\n"
                      "2.   E-mail anónimo\n"
                      "\n")

    switch = {'1':option_1,
              '2': anonMailer,
              99: error
              }
    try:
        switch[input]()
    except KeyError:
        switch[99]()

def option_2():
    print()

def error():
    print("La opción seleccionada no está disponible. Selecciona un valor de entre los siguientes")
    init()

def init():
    input = raw_input("1.   Mailing\n"
                      "2.   Flood anónimo en diversos foros\n"
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

def main():

    print ("Bienvenido al FrameWork.\n"
           "Aquí están las opciones disponibles:\n")

    init()



if __name__ == "__main__":
    main()