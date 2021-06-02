num = 0
while True:
    print('-'*30)
    num = int(input('Digite um número para ver sua tabuada de multiplicação: '))
    if num < 0:
        break
    print('-' * 30)
    print ('{} x {} = {}'.format(num, 1, num*1))
    print ('{} x {} = {}'.format(num, 2, num*2))
    print ('{} x {} = {}'.format(num, 3, num*3))
    print ('{} x {} = {}'.format(num, 4, num*4))
    print ('{} x {} = {}'.format(num, 5, num*5))
    print ('{} x {} = {}'.format(num, 6, num*6))
    print ('{} x {} = {}'.format(num, 7, num*7))
    print ('{} x {} = {}'.format(num, 8, num*8))
    print ('{} x {} = {}'.format(num, 9, num*9))
    print ('{} x {} = {}'.format(num, 10, num*10))
print('Programa encerrado!!!')