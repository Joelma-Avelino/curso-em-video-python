n = int(input('Digite um número: '))
mult=0

for count in range(2, n):
    if (n % count == 0):
        print('Múltiplo de',count)
        mult += 1
if(mult==0):
    print('É primo')
else:
    print('Tem',mult,'Múltiplos acima de 2 e abaixo de',n)