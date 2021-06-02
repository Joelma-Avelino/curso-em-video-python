jurosTotal = 0
saldoDevedor = float(input('Qual valor de crédito em R$ que o banco aprovou? '))
parcelas = int(input('Em quantas parcelas será pago o valor do empretimo? '))
jurosAoMes = float(input('Quanto de juros ao mês será pago ao banco? '))
amortizacao = saldoDevedor / parcelas

for mes in range(0, parcelas):
    juros = saldoDevedor * (jurosAoMes/100)
    prestacao = amortizacao + juros
    saldoDevedor = saldoDevedor - amortizacao

    print('NO MÊS {} SALDO DEVEDOR É DE R$ {} - {} QUE É O VALOR DA PARCELA.'.format(mes+1,saldoDevedor, prestacao))

    jurosTotal += juros

totalDaAmortizacao = amortizacao * parcelas
total = totalDaAmortizacao + jurosTotal

print('Valor total da amortização R$ {}'.format(totalDaAmortizacao))
print('Valor total dos juros R$ {}'.format(jurosTotal))
print('Valor total a ser pago ao banco R$ {}'.format(total))
