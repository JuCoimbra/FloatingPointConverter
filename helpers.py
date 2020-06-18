from decimal import *
import platform
import os

def get_integer_input(prompt):
    while True:
        try:
            res = int(input(prompt + ': \n'))
            break
        except (ValueError, NameError):
            print("A seleção deve ser numérica.")
    return res

def get_float_input(prompt):
    while True:
        try:
            res = float(input(prompt + ': \n'))
            break
        except (ValueError, NameError):
            print("A seleção deve ser numérica.")
    return res

def get_decimal_input(prompt):
    while True:
        try:
            res = Decimal(input(prompt + ': \n'))
            break
        except (ValueError, NameError):
            print("A seleção deve ser numérica.")
    return res


def clrscr():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

def newline():
    print('\n')