nome = str(input('Digite o seu nome completo: ')).strip()


nome = nome.split()

st = nome[0]
posicao = len(nome) - 1
la = nome[posicao]

print('Primero nome: {}\nÚltimo nome: {}'.format(st, la))