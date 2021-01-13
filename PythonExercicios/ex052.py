numero = int(input('Digite um número inteiro: '))

total = 0

for i in range(0, numero):
    if numero % (i + 1) == 0:
        print('\033[33m', end=' ')
        total += 1
    else:
        print('\033[31m', end=' ')

    print(f'{i + 1}', end=' ')

print(f'\n\033[mO número {numero} foi divisível {total} vezes')

if total == 2:
    print(f'{numero} é um número primo!')
else:
    print(f'{numero} não é um número primo!')
