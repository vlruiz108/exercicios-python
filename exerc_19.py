from random import choice

a1 = str(input("Escreva o primeiro nome "))
a2 = str(input("Escreva o segundo nome "))
a3 = str(input("Escreva o terceiro nome "))
a4 = str(input("Escreva o quarto nome "))
list = [a1, a2, a3, a4]

escolha = choice(list)
print("O aluno escolhido foi {}" .format(escolha))