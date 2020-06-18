import sys
import os
import FloatPoint as f
import DoublePoint as d
import helpers


def main_menu():

    print("Selecione o tipo de operação que deseja fazer")
    print("1 - Converter um número para precisão simples - 32bits")
    print("2 - Converter um número para precisão dupla - 64bits")
    print("3 - Sair")
    choice = helpers.get_integer_input("Digite a sua escolha: ")

    if choice == 1:
        helpers.clrscr()
        number = helpers.get_float_input(
            "Digite o número a ser convertido: ")
        outcome = f.float_converter(number)
        signal, exponent, mantissa = outcome.split(".")
        hex = float.hex(number)
        print(f"Sinal: {signal} Expoente: {exponent} Mantissa: {mantissa}")
        print(f"Binário: {signal}{exponent}{mantissa}")
        print(f"Hexadecimal: {hex}\n")
        helpers.waitForKeypress()
        helpers.clrscr()

    if choice == 2:
        helpers.clrscr()
        number = helpers.get_float_input(
            "Digite o número a ser convertido: ")
        outcome = d.Double_converter(number)
        signal, exponent, mantissa = outcome.split(".")
        hex = float.hex(number)
        print(f"Sinal: {signal} Expoente: {exponent} Mantissa: {mantissa}")
        print(f"Binário: {signal}{exponent}{mantissa}")
        print(f"Hexadecimal: {hex}\n")
        helpers.waitForKeypress()
        helpers.clrscr()

    if choice == 3:
        return True
    else:
        return False


def main():
    exitflag = False
    helpers.clrscr()
    while exitflag is False:
        exitflag = main_menu()


main()
