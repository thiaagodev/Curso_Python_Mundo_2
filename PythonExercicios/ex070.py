total = quantidade_produtos_custam_mais_de_mil = 0
nome_produto_mais_barato = ''
produto_mais_barato = 9999999999999999

while True:
    nome = input('Qual o nome do produto? ')
    preco = float(input(f'Informe o preço de {nome}: '))

    total += preco
    if preco > 1000:
        quantidade_produtos_custam_mais_de_mil += 1
    if preco < produto_mais_barato:
        nome_produto_mais_barato = nome
        produto_mais_barato = preco

    continuar = input('Deseja continuar? [S / N]: ').upper()[0]
    if continuar in 'Nn':
        break

print('-'*30)
print(f'Total gasto: {total}')
print(f'{quantidade_produtos_custam_mais_de_mil} produtos custam mais de R$1000')
print(f'O produto mais barato é {nome_produto_mais_barato} que custa R${produto_mais_barato}')
print('-'*30)
