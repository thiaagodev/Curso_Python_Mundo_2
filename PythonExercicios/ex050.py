valor = 0

for i in range(0, 6):
    numero = int(input(f'Digite o {i + 1}° valor: '))
    if numero % 2 == 0:
        valor += numero
    else:
        print(f'{numero} é impar')

print(f'Valor total dos números pares informados: {valor}')
