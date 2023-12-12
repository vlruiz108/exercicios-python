'''
Escreva um programa que leia a velocidade de um carro.
'''
velocidade = float(input("Velocidade do carro: "))
if velocidade > 80:
    print("Você foi multado, exedeu o limite de velocidade")
    multa = (velocidade - 80)*7
    print("Sua velocidade foi {} e sua multa será de R$ {:.2f}".format(velocidade, multa))
else:
    print("Tenha um bom dia, dirija com segurança!")
    