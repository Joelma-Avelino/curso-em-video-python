n = s = c = 0
while n != 999:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    c += 1
    s += n
print('A soma dos {} valores foi {}'.format(c,s))
