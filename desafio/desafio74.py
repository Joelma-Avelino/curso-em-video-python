from random import randint
n = (randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10))
print('Eu sorteei os valores {}'.format(n))
print('O maior valor sorteado foi {}'.format(max(n)))
print(('O menor valor sorteado foi {}'.format(min(n))))