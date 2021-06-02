from random import randint
computador = randint(0, 5) #faz o computador pensar
print('-=-'*20)
print('Vou pensar em um número entre 0 e 5. Tente advinhar...')
print('-=-'*20)
jogador = int(input('Em que número eu pensei? ')) # o jogador tenta advinhar
if jogador == computador:
    print('Acertou,parabéns')
else:
    print('Errou,Eu ganhei pensei no número {} e não no número {}'.format(computador, jogador))




