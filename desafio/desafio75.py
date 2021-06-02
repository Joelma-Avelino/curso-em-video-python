num = (int(input('Digite um número: ')),
        int(input('Digite um número: ')),
        int(input('Digite um número: ')),
        int(input('Digite um número: ')))

print('Você digitou os valores {}'.format(num))
print('O número 9 apareceu {} vezes'.format(num.count(9)))
if 3 in num:
    print('O número 3 está na posição {}'.format(num.index(3)))
else:
    print('O valor 3 não foi digitado')
print('Os valores pares digitados foram ', end='')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')
