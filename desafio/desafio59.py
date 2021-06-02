n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
opção = 0
while opção!= 5:

    print('''Escolha a opção desejada:
    [ 1 ] SOMAR
    [ 2 ] MULTIPLICAR
    [ 3 ] MAIOR
    [ 4 ] NOVOS NÚMEROS
    [ 5 ] SAIR DO PROGRAMA''')

    opção = int(input('>>>>>>>>>> Qual é a sua opção? '))
    if opção == 1:
        total = n1 + n2
        print('A soma de {} + {} = {}'.format(n1,n2,total))

    elif opção == 2:
        total = n1 * n2
        print('A multiplicação de {} x {} = {}'.format(n1, n2, total))

    elif opção == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('Entre {} e {} o maior valor é {}'.format(n1,n2,maior))1010

    elif opção == 4:
        print('Informe os números novamente:')
        n1 = int(input('Digite o primeiro valor: '))
        n2 = int(input('Digite o segundo valor: '))

    elif opção == 5:
        print('Finalizando...')

    else:
        print('Opção inválida. Tente novamente')
    print('=-='*10)


print('Fim do programa!Volte sempre!')
