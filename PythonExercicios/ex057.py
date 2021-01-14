sexo = input('Informe seu sexo Feminino[F] | Masculino[M]: ').upper()[0]
while sexo not in 'MmFf':
    sexo = input('Você informou um valor inválido! Por favor digite novamente: ').upper()

print('Ok')
