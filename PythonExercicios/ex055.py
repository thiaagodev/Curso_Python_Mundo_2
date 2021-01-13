maior_peso = 0
menor_peso = 0

for i in range(0, 5):
    peso = float(input('Digite seu peso: '))
    if i == 0:
        maior_peso = peso
        menor_peso = peso

    if peso > maior_peso:
        maior_peso = peso
    elif peso < menor_peso:
        menor_peso = peso

print(f'O menor peso foi {menor_peso} e o maior foi {maior_peso}')
