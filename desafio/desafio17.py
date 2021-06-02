import math

cato = float(input('Qual o comprimento do cateto oposto? '))
cata = float(input('Qual o comprimento do cateto adjacente? '))

# hipo = ((cato**2) + (cata**2)) ** (1/2)
hipo = math.sqrt((cato**2) + (cata**2))

print('CATETO OPOSTO É {} CATETO ADJACENTE É {} LOGO A HIPOTENUSA É {}'.format(cato, cata, hipo))
