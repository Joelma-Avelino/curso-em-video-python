from datetime import date
atual = date.today().year
nasc = (int(input('EM QUAL ANO VOCÊ NASCEU? ')))
idade = atual - nasc

if idade <= 9:
    print('CATEGORIA MIRIM')
elif idade <= 14:
    print('CATEGORIA INFANTIL')
elif idade <= 19:
    print('CATEGORIA JUNIOR')
elif idade <= 20:
    print('CATEGORIA SÊNIOR')
else:
    print('CATEGORIA MASTER')
