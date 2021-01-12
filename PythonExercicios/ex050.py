valor = 0

for i in range(0, 6):
    numero = int(input('Digite um número inteiro: '))
    if numero % 2 == 0:
        valor += numero
    else:
        print(f'{numero} é impar')

print(f'Valor total : {valor}')
