primeiro = float(input('Digite um número: '))
segundo = float(input('Digite outro número: '))
terceiro = float(input('Digite mais um número: '))

maior = primeiro
if (segundo > maior):
    maior = segundo
if (terceiro > maior):
    maior = terceiro
print('Maior',maior)

menor = primeiro
if (segundo < menor):
    menor = segundo
if (terceiro < menor):
    menor = terceiro
print('Menor',menor)
