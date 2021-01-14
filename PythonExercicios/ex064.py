numero = 0
soma = 0
count = -1

while numero != 999:
    numero = int(input('Digite um número: '))
    if numero != 999:
        soma += numero
    count += 1

print(f'Você digitou {count} números e a soma total foi {soma}')
