times = ('America','Atletico paranaense','Atletico - GO','Atletico - MG','Bahia','Ceará','Chapecoense','Corinthias','Cuiabá','Flamengo',
         'Fluminense','Fortaleza','Grêmio','Internacional','Juventude','Palmeiras','Red bull bragantino','Santos','São Paulo','Sport')

for cont in range(0, len(times)):
    print('='*30)
    print(f'Na posição {cont + 1} está o time {times[cont]}')

print('='*30)
print(f'Os primeiros 5 colocados são {times[0:5]}')
print('>>>>>>>>>>>>>>><<<<<<<<<<<<<<<')
print(f'Os 4 últimos colocados {times[-4:]}')
print('>>>>>>>>>>>>>>><<<<<<<<<<<<<<<')
print(f'Os times em ordem álfabetica: {sorted(times)}')
print('>>>>>>>>>>>>>>><<<<<<<<<<<<<<<')
print(f'A chapecoense está na {times.index("Chapecoense")+1} posição')
