#velocidade = int(input('Qual a velocidade do carro: ')).strip()
#if velocidade >= 80:
 #   print('VOCÊ ULTRAPASSOU O LIMITE DE VELOCIDADE!Sua multa foi de {}'.format(multa))
#else:
 #   print('VOCÊ RESPEITOU O LIMITE,PARABÉNS!')
#multa = (velocidade - 80)*7

velocidade = float(input('Qual é a velocidade atual do carro? '))

if velocidade >= 80:
    print('MULTADO! Você ultrapassou o limite de velocidade que é 80km/h')
    multa = (velocidade - 80) * 7
    print('Você deve pagar uma multa de {}'.format(multa))
print('Tenha um bom dia! Dirija com segurança!')



