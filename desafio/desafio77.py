p = ('GAS','AMERICANO','JOELMA','ORLANDO','TESOURA','QUADRO','PICASSO')
for palavra in p:
    print(f'\nNa palavra {palavra} temos 2',end='')
    for letra in palavra:
        if letra.upper() in 'AEIOU':
            print(letra, end='')