real = float(input('Quanto dinheiro você tem na carteira?R$ '))
dolar = real / 5.37
euro = real /  6.51
print('Com R${:.2f} você pode comprar U${:.2f} e {:.2f} em € '.format(real, dolar,euro))
