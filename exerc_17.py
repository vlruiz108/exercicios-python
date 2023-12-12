from math import hypot

co = float(input("Digite o cateto oposto "))
ca = float(input("Agora digite o cateto adjacente "))
hi = hypot(co, ca)
print("O cateto da hipotenusa é {:.2f}" .format(hi))