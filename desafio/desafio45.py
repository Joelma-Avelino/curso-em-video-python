from random import randint
itens = ('pedra', 'papel', 'tesoura')
computador = randint(0,2)
print(''' Suas opções:
[ 0 ] pedra
[ 1 ] papel
[ 2 ] tesoura ''')
jogador = int(input('QUAL É SUA JOGADA?'))
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))




