from random import randint

vitorias = 0

while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(0, 10)
    total = jogador + computador

    tipo = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]

    print('Você jogou {} e o computador {} o total foi {}'.format(jogador, computador, total))

    if tipo == 'P':
        if total % 2 == 0:
            print('Você VENCEU.')
            vitorias += 1
        else:
            print('Você PERDEU')
            break
    elif tipo == 'I':
        if total % 2 != 0:
            print('Você VENCEU.')
            vitorias += 1
        else:
            print('Você PERDEU')
            break

    print('Vamos jogar novamente...')

print('GAME OVER, VOCÊ VENCEU {} VEZES'.format(vitorias))
