salario = float(input('Qual seu atual salário bruto? '))

if salario <= 1250:
    novo = salario + (salario * 15 / 100)
    print('Você terá um aumento de 15% no seu salário,logo seu atual valor a receber é {}'.format(novo))
else:
    novo = salario + (salario * 10 / 100)
    print('Você terá um aumento de 10% no seu salário,logo seu atual valor a receber é {}'.format(novo))


