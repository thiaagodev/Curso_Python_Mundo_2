from datetime import date

ano = int(input('Digite seu ano de nascimento: '))

idade = date.today().year - ano

if idade <= 9:
    print(f'Você tem {idade} anos, portanto você é Mirim')
elif idade > 9 and idade <= 14:
    print(f'Você tem {idade} anos, portanto você é Infantil')
elif idade > 14 and idade <= 19:
    print(f'Você tem {idade} anos, portanto você é Junior')
elif idade > 19 and idade <= 20:
    print(f'Você tem {idade} anos, portanto você é Sênior')
else:
    print(f'Você tem {idade} anos, portanto você é Master')
