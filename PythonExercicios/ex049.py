numero = int(input('Informe um número inteiro: '))

print('A tabuada de {} é: '.format(numero))

print('-' * 15)

for i in range(0, 10):
    print(f'{numero} x {i + 1:2} = { numero * (i + 1):3}')

print('-' * 15)
