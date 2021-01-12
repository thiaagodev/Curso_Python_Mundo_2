from datetime import date

ano = int(input('Informe o seu ano de nascimento: '))
ano_atual = date.today().year
idade = ano_atual - ano

if idade < 18:
    print(f'Você tem {idade} anos, portanto ainda vai se alistar ao serviço militar.')
    print(f'Faltam {(idade - 18) * -1} anos para você se alistar, você irá se alistar em {ano_atual + ((idade - 18) * -1)}')
elif idade == 18:
    print(f'Você tem {idade} anos, já está na hora de se alistar!')
else:
    print(f'Já passou da hora de se alistar! você tem {idade} anos, portanto você está {idade - 18} anos atrasado')
