valor_casa = float(input('Qual o valor da casa? '))
salario = float(input('Qual o salário do comprador? '))
anos = int(input('Em quantos anos vai pagar? '))

prestacao_mensal = valor_casa / (anos * 12)

if prestacao_mensal <= salario * (30 / 100):
    print('Empréstimo aprovado!')
else:
    print('Empréstimo não aprovado! o valor da prestação é {:.2f} e excede os 30% do seu salário'.format(prestacao_mensal))
