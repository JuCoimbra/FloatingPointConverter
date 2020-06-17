import sys
import os
import FloatPoint as f
import DoublePoint as d

def input_integer(message):
	try:
		numberI = int(input(message))
	except ValueError:
		print("Por favor, digite um número!")
		return input_integer(message)
	else:
		return numberI

def input_Decimal(message):
	try:
		numberF = float(input(message))
	except ValueError:
		print("Por favor, digite um número ou tente colocar um ponto no lugar da virgula!")
		return input_Decimal(message)
	else:
		return numberF


def main_menu():

	print("Selecione o tipo de operação que deseja fazer")
	print("1 - Converter um número para precisão simples - 32bits")
	print("2 - Converter um número para precisão dupla - 64bits")
	print("3 - Sair")
	choice = input_integer("Digite a sua escolha: ")

	if choice == 1:
		exitflag = False
		number = input_Decimal("Digite o número a ser convertido: ")
		outcome = f.float_converter(number)
		signal, exponent, mantissa = outcome.split(".")
		hex = float.hex(number)
		print(f"Sinal: {signal} Expoente: {exponent} Mantissa: {mantissa}")
		print(f"Binário: {signal}{exponent}{mantissa}")
		print(f"Hexadecimal: {hex}\n")

	if choice == 2:
		exitflag = False
		number = input_Decimal("Digite o número a ser convertido: ")
		outcome = d.Double_converter(number)
		signal, exponent, mantissa = outcome.split(".")
		hex = float.hex(number)
		print(f"Sinal: {signal} Expoente: {exponent} Mantissa: {mantissa}")
		print(f"Binário: {signal}{exponent}{mantissa}")
		print(f"Hexadecimal: {hex}\n")

	if choice == 3:
		return True
	else:
		return False


def main():
	exitflag = False
	while exitflag is False:
		os.system('cls') or None
		exitflag = main_menu()

main()
