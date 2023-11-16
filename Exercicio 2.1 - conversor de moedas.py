#Conversor de MOEDAS

print('.'*50)
print ('Conversor de moedas:')
print('*'*35)
real = float (input('Qual o valor em Reais você quer converter? R$ '))

dolar = real / 4.8664
print ('R$ {:.2f} convertido para Dolar Americano = US$ {:.2f}'.format (real, dolar))
print('.'*35)

euro = real / 5.1988
print ('R$ {:.2f} convertido para Euro = Euro {:.2f}'.format (real, euro))
print('.'*35)

libra_esterlina = real / 5.9847
print ('R$ {:.2f} convertido para Libra Esterlina GBP {:.2f}'.format (real, libra_esterlina))
print('.'*35)

dolar_canadense = real / 3.5392
print ('R$ {:.2f} convertido para Dólar Canadense (CAD) {:.2f}'.format (real, dolar_canadense))
print('.'*35)

peso_argentino = real / 0.00139
print ('R$ {:.2f} convertido para Peso Argentino (ARS) {:.2f}'.format (real, peso_argentino))
print('.'*35)

peso_chileno = real / 0.0055
print ('R$ {:.2f} convertido para Peso Chileno (CLP) {:.2f}'.format (real, peso_chileno))
print('.'*35)

peso_mexicano = real / 0.2776
print ('R$ {:.2f} convertido para Peso Mexicano (MXC) {:.2f}'.format (real, peso_mexicano))
print('.'*50)