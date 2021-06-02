distancia = float(input('Qual a distância em km da viajem: '))
if distancia <= 200:
    print('A passagem referente a viajem de {} é R$0,50 por km/h'.format(distancia))
    valor = distancia * 0.50
    print('O valor a pagar é de R$ {}'.format(valor))
else:
    print('A passagem referente a viajem de {} é R$0,45 por km/h'.format(distancia))
    valor = distancia * 0.45
    print('O valor a pagar é de R$ {}'.format(valor))
