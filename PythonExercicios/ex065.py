continuar = 'S'
maior_numero = 8888888888
menor_numero = 0
soma = 0
count = 0

while continuar == 'S':
    numero = int(input('Insira um número: '))
    if numero > maior_numero:
        maior_numero = numero
    if numero < menor_numero:
        menor_numero = numero
    soma += numero
    count += 1

    continuar = input('Deseja continuar? [S / N] ').upper()

print(f'A média total dos valores informados é {soma / count}')
print(f'O maior número foi {maior_numero} e o menor {menor_numero}')
