primeiro_elemento = int(input('Informe um número: '))
elementos = int(input('Quantos elementos da sequência de fibonacci você quer ver? '))

elemento_anterior = primeiro_elemento
elemento_anterior_anterior = primeiro_elemento - 1

print(f'{primeiro_elemento - 1 }, {primeiro_elemento} ', end=', ')

while elementos > 1:
    proximo_elemento = elemento_anterior + elemento_anterior_anterior
    print(proximo_elemento, end=', ')

    elemento_anterior_anterior = elemento_anterior
    elemento_anterior = proximo_elemento

    elementos -= 1
