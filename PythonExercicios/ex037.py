numero = int(input('Escreva um número inteiro qualquer: '))
escolha = int(input('Escolha qual será a base de conversão: - 1 para binário; - 2 para octal e 3 para hexadecimal: '))

if escolha == 1:
    print('O número {} em binário fica: {}'.format(numero, bin(numero)[2:]))
elif escolha == 2:
    print('O número {} em octal fica: {}'.format(numero, oct(numero)))
elif escolha == 3:
    print('O número {} em hexadecimal fica: {}'.format(numero, hex(numero)))
else:
    print('Essa opção não existe! digite uma opção existente.')
