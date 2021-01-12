frase = str(input('Digite uma frase: '))

sem_espacos = frase.replace(' ', '')

if ''.join(reversed(sem_espacos)) == sem_espacos:
    print(f'"{frase}" é um palíndromo!')
else: 
    print(f'"{frase}" não é um palíndromo!')
