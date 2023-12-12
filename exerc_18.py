from math import sin, radians, cos, tan
angulo = float(input("Digite um número para angulo "))
seno = sin(radians(angulo))
print("O angulo é {} e o seno {:.2f}" .format(angulo, seno))
cosseno = cos(radians(angulo))
print("O cosseno é {:.2f}" .format(cosseno))
tangente = tan(radians(angulo))
print(" O angulo é {} e a tangente {:.2f}".format(angulo, tangente))