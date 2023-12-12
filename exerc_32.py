from datetime import date

ano_bi = int(input("Digite um ano: "))
if ano_bi == 0:
    ano_bi = date.today().year
    print("ano atual")
if ano_bi % 4 == 0 and (ano_bi % 100 != 0 or ano_bi % 400 == 0):
    print("Esse ano {} é bissesto".format(ano_bi))
else:
    print("Esse ano {} não é bissexto ".format(ano_bi))
    