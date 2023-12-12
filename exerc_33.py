#Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
# Path: exerc_34.py
#
num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))
num3 = int(input("Digite mais um número: "))
# Verificando o menor número
menor = num1
if num2 < num1 and num2 < num3:
    menor = num2
if num3 < num1 and num3 < num2:
    menor = num3
# Verificando o maior número
maior = num1
if num2 > num1 and num2 > num3:
    maior = num2
if num3 > num1 and num3 > num2:
    maior = num3
# Mostrando o resultado
print("O menor número digitado foi {}".format(menor))
print("O maior número digitado foi {}".format(maior))
