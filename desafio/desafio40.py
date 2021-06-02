n1 = float(input('QUAL A PRIMEIRA NOTA: '))
n2 = float(input('QUAL A SEGUNDA NOTA: '))
media = (n1 + n2) / 2

if media < 5:
    print('REPROVADO,estude mais!')
elif media <= 6.9:
    print('RECUPERAÇÃO, boa sorte!')
elif media >= 7:
    print('APROVADO, parabéns!')
