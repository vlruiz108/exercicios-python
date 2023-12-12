n1 = float(input("Digite a primeira nota "))
n2 = float(input("Digite a segunda nota "))
media = (n1 + n2) / 2
print("A primeira nota foi {}, a segunda {} a média {:.2f}" .format(n1, n2, media))
if media >=6.0:
    print("Sua {} isso é muito bom parabéns!".format(media))
else:
    print("Sua média é {} bora para re cuperação".format(media))