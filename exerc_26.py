nome = str(input("Digite um nome ")).upper().strip()
print("A letra A para apareceu {}" .format(nome.count('A')))
print("A primeira letra a aparece na posição {}" .format(nome.find('A')+1))
print("A ultima posição da letra a {}" .format(nome.rfind('A')+1))