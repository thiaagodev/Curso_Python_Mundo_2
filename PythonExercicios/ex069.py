pessoas_mais_de_dezoito_anos = 0
mulheres_menos_de_vinte_anos = 0
quantidade_homens = 0

while True:
    idade = int(input('Qual a sua idade: '))
    sexo = input('Qual o seu sexo? [F / M]: ').upper()[0]

    if idade > 18:
        pessoas_mais_de_dezoito_anos += 1
    if sexo in 'Ff' and idade < 20:
        mulheres_menos_de_vinte_anos += 1
    if sexo in 'Mm':
        quantidade_homens += 1
    
    continuar = input('Deseja continuar? [S / N]: ').upper()[0]
    if continuar in 'Nn':
        break

print('-'*30)
print(f'Foram cadastrados {pessoas_mais_de_dezoito_anos} pessoas com mais de 18 anos')
print(f'{mulheres_menos_de_vinte_anos} mulheres com menos de 20 anos')
print(f'{quantidade_homens} homens.')
print('-'*30)
