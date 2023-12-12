#Escreva um programa que faça o computador “pensar” em um número inteiro entre
# 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo 
#computador. 
# O programa deverá escrever na tela se o usuário venceu ou perdeu
from random import randint
from time import sleep

escolha = int(input("Que número pensei de 0 a 5: "))
print("Processando...")
sleep(3)
computador = randint(0,5)
if computador == escolha:
    print("Você escolheu número {}, acertou!".format(computador))

else:
    print("Errou o número que escolhi foi {}".format(computador))
