print('>>>>>>>>>>DESCUBRA SUA MÉDIA NA UNIASSELVI<<<<<<<<<<')
n1 = int(input('Qual a nota da primeira prova? '))
n2 = int(input('Qual a nota da segunda prova? '))
n3 = int(input('Qual a nota da terceira prova? '))
n4 = int(input('Qual a nota da quarta prova? '))

t1 = n1 * 1.5
t2 = n2 * 1.5
t3 = n3 * 4
t4 = n4 * 3

total = (t1 + t2 + t3 + t4)/10

print('Levando em consideração as notas observadas pelo sistema sua média é {}'.format(total))