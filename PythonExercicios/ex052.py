numero = int(input('Digite um número inteiro: '))

contador = 0

for i in range(0, numero):
    if numero % (i + 1) == 0:
        contador += 1

if contador == 2:
    print(f'{numero} é um número primo!')
else:
    print(f'{numero} não é um número primo!')
