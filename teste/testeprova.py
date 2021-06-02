print('-'*30)
print('CALCULO DE MÉDIA ESCOLAR')
print('-'*30)
nota1 = float(input('Qual foi sua primeira nota? '))
nota2 = float(input('Qual foi sua segunda nota? '))
media = (nota1 + nota2) / 2
print('Sua média foi {}'.format(media))
if media >= 7:
    print('Aprovado.Parabéns!!!')
else:
    print('Reprovado, estude mais')

