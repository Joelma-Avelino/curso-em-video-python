km = int(input('QUANTOS KM FORAM PECORRIDOS? '))
dias = int(input('QUAL A QUANTIDADE DE DIAS QUE PASSOU COM O CARRO? '))
vkm = km * 0.15
vdias = dias * 60
vtotal = vkm + vdias
print('com {}km rodados e {} dias de uso o valor total é de {}'.format(km, dias, vtotal))
