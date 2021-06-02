r1 = float(input('PRIMEIRO SEGMENTO: '))
r2 = float(input('SEGUNDO SEGMENTO: '))
r3 = float(input('TERCEIRO SEGMENTO: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima podem formar um triângulo ', end='')
    if r1 == r2 == r3:
        print('EQUILÁTERO')
    elif r1 != r2 != r3 != r1:
        print('ESCALENO')
    else:
        print('ISÓSCELES')

else:
    print('Os segmentos acima não podem formar triângulo')
