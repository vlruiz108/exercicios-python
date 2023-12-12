
r1 = float(input("Digite primeira reta "))
r2 = float(input("Digite a segunda reta "))
r3 = float(input("Digite a terceira reta "))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('As retas de acima podem formar um triagulo')
else:
    print('As retas acima não podem formar um triangulo')
