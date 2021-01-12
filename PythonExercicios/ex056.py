nome_homem_mais_velho = ''
idade_homem_mais_velho = 0
mulheres_menos_de_20 = 0
idade_total = 0

for i in range(0, 4):
    nome = input('Digite seu nome: ')
    idade = int(input('Digite sua idade: '))
    sexo = input('Digite seu sexo: Feminino[F] | Masculino[M]: ')
    idade_total += idade
    if sexo == 'M' and idade > idade_homem_mais_velho:
        idade_homem_mais_velho = idade
        nome_homem_mais_velho = nome
    if sexo == 'F' and idade < 20:
        mulheres_menos_de_20 += 1

print(f'A média de idade do grupo é: {idade_total / 4}')
print(f'O homem mais velho é {nome_homem_mais_velho}')
print(f'{mulheres_menos_de_20} mulheres tem menos de 20 anos')
