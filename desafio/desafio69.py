tot18 = homem = m20 = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [F/M]: ')).strip().upper()[0]
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        homem += 1
    if  sexo == 'F' and idade < 20:
        m20 += 1

    opcao = ' '
    while opcao not in 'SN':
         opcao =  str(input('Quer continuar?[S/N]: ')).strip().upper()[0]
    if opcao == 'N':
        break
print('Total de pessoas maiores de 18 anos {}.'.format(tot18))
print('Total de homens cadastrados foi {}.'.format(homem))
print('O total de mulheres menor de 20 anos é {}.'.format(m20))
