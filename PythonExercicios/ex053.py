frase = str(input('Digite uma frase: '))

sem_espacos = frase.replace(' ', '')

inverso = ''

for letra in range(len(sem_espacos) -1, -1, -1):
    inverso += sem_espacos[letra]

print(f'O inverso de {frase} é {inverso}')

if inverso == sem_espacos:
    print(f'"{frase}" é um palíndromo!')
else: 
    print(f'"{frase}" não é um palíndromo!')
