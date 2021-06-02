nome = str(input('Qual é o seu nome?')).upper()
if nome == 'GUSTAVO':
    print('Que nome bonito!')
elif nome == 'PEDRO' or nome == 'MARIA' or nome == 'PAULO':
    print('Seu nome é bem normal no Brasil')
elif nome in 'ANA CLAUDIA JESSICA':
    print('Belo nome feminino')
else:
    print('Seu nome é bem normal.')
print('Tenha um bom dia {}'.format(nome))