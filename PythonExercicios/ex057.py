sexo = input('Informe seu sexo Feminino[F] | Masculino[M]: ').upper()
while sexo != 'M' and sexo != 'F':
    sexo = input('Você informou um valor inválido! Por favor digite novamente: ').upper()

print('Ok')
