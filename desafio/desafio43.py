peso = float(input('QUAL O SEU PESO?(KG) '))
altura = float(input('QUAL A SUA ALTURA?(M) '))
imc = peso / (altura * altura)

if imc < 18.5:
    print('SEU IMC É {:.2f} E VOCÊ ESTÁ ABAIXO DO PESO'.format(imc))
elif imc <= 25:
    print('SEU IMC É {:.2f} E VOCÊ ESTÁ COM O PESO IDEAL'.format(imc))
elif imc <= 30:
    print('SEU IMC É {:.2f} E VOCÊ ESTÁ SOBREPESO'.format(imc))
elif imc <= 40:
    print('SEU IMC É {:.2f} E VOCÊ ESTÁ OBESO'.format(imc))
else:
    print('SEU IMC É {:.2f} E VOCÊ ESTÁ COM OBESIDADE MÓRBIDA'.format(imc))

