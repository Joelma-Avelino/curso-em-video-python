print('{:=^40}'.format('LOJAS JOELMA'))
preco = float(input('Qual o valor do produto?R$ '))

print('''Escolha a forma de pagamento:
[ 1 ] a vista dinheiro ou cheque
[ 2 ] a vista no cartão
[ 3 ] em até 2x no cartão
[ 4 } em 3x ou mais no cartão ''')

opção = int(input('Sua opção: '))

if opção == 1:
    valor = preco - (preco * 10 / 100)
    print('O produto de R$ {} com 10% de desconto sai por R$ {}  '.format(preco, valor))
elif opção == 2:
    valor = preco - (preco * 5 / 100)
    print('O produto de R$ {} com 5% de desconto sai por R$ {}  '.format(preco, valor))
elif opção == 3:
    parcela = preco / 2
    print('O produto de R$ {} mantem o preço original'.format(preco))
    print('Sua compra será parcelada em 2x de R$ {:.2f} SEM JUROS'.format(parcela))
elif opção == 4:
    valor = preco + (preco * 20/ 100)
    totparc = int(input('Quantas parcelas? '))
    parcela = valor / totparc
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS DE 20%'.format(totparc, parcela))
    print('O produto de R$ {} com 20% de juros sai por R$ {}  '.format(preco, valor))




