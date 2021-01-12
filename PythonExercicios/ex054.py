maioridade = 0
menor_idade = 0

for i in range(0, 7):
    idade = int(input('Digite sua idade: '))
    if(idade >= 21):
        maioridade += 1
    else:
        menor_idade += 1

print(f'{maioridade} pessoas são de maior e {menor_idade} são de menor')
