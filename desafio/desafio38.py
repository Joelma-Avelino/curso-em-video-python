n1 = int(input('Digite um número inteiro: '))
n2 = int(input('Digite outro inteiro: '))

if n1 > n2:
    print('O primeiro valor é maior ')
elif n2 > n1:
    print('O segundo valor é maior')
elif n1 == n2:
    print('Não existe valor maior, os dois são iguais')
