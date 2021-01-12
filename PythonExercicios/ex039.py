from datetime import date

ano = int(input('Informe o seu ano de nascimento: '))
ano_atual = date.today().year
idade = ano_atual - ano

if idade < 18:
    print('Você tem {} anos, portanto ainda vai se alistar ao serviço militar.'.format(idade))
    print('Faltam {} anos para você se alistar'.format((idade - 18) * -1))
elif idade == 18:
    print('Você tem {} anos, já está na hora de se alistar!'.format(idade))
else:
    print('Já passou da hora de se alistar! você tem {} anos, portanto você está {} anos atrasado'.format(idade, idade - 18))
