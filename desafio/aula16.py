lanche = ('Hambúrguer','suco','pizza','pudim')

for comida in lanche:
    print('Eu vou comer {}'.format(comida))

for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')

for pos,comida in enumerate(lanche):
    print('Eu vou comer {} na posição {}'.format(comida, pos))
print('Comi para caramba')