tabuada = int(input('Qual número deseja ver a tabuada? '))
for cont in range(0, 11):
    total = cont * tabuada
    print('''{} x {} = {}'''.format(tabuada, cont, total))