total = t1000 = menor = cont = 0
barato = ' '
while True:
    nome = str(input('Qual o nome do produto? ')).upper().strip()
    preco = float(input('Qual o valor do produto [R$]: '))
    cont += 1
    total += preco
    if preco > 1000:
        t1000 += 1
    if cont == 1:
        menor = preco
        barato = nome
    else:
        if preco < menor:
            menor = preco
            barato = nome
    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('Quer continuar?[S/N]: ')).strip().upper()[0]
    if opcao == 'N':
        break
print('{:-^40}'.format(' FIM DO PROGRAMA '))
print('O total da compra foi R$ {:.2f}.'.format(total))
print('O total de produtos acima de R$ 1000 foi {}'.format(t1000))
print('O produto mais barato foi {} que custa R$ {:.2f}'.format(barato,menor))

