numero = int(input('Informe um número inteiro: '))

print('A tabuada de {} é: '.format(numero))

print('-' * 11)

for i in range(0, 10, 1):
    print('{} x {:2} = {}'.format(numero, i + 1, numero * (i + 1)))

print('-' * 11)
