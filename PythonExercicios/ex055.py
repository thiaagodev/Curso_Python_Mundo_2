maior_peso = 0
menor_peso = 0
peso_anterior = 0

for i in range(0, 5):
    peso = float(input('Digite seu peso: '))
    if peso > peso_anterior:
        maior_peso = peso
    elif peso < peso_anterior:
        menor_peso = peso
        
    peso_anterior = peso

print(f'O menor peso foi {menor_peso} e o maior foi {maior_peso}')
