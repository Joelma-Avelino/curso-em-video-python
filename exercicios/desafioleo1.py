
nome = str(input('Nome: ')).strip().upper()
notas = []
total = 0

for n in range(1, 8):
    nota = float(input('Qual a {}ª nota: '.format(n)))
    notas.append(nota)
    total = total + nota

menor = min(notas)
maior = max(notas)
media = (total - (menor + maior)) / 5

print('O nome do atleta é: {}'.format(nome))
print('A maior nota é {}, a menor nota é {}'.format(menor, maior))
print('A média das notas foi: {}'.format(media))




