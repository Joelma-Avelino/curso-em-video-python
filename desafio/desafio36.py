casa = float(input('Qual valor da casa?R$ '))
salario = float(input('Qual valor do salário?R$ '))
anos = int(input('Quantos anos de financiamento:'))
parcela = casa / (anos * 12)

if parcela <= salario - (salario * 30/100):
    print('Crédito aprovado, as parcelas ficaram por R$ {}'.format(parcela))
else:
    print('Reprovado, tente outras opções')

