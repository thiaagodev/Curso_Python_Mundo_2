print('O produto custa R$256, qual método de pagamento deseja?')
opcao = int(input('Digite: 1 - a vista dinheiro/cheque | 2 - a vista no cartão | 3 - em até 2x no cartão | 4 - 3x ou mais no cartão'))

if opcao == 1:
    print(f'Você escolheu pagar a vista no dinheiro, então o desconto é de 10%, valor total: R${256 - (256 * 0.10)}')
elif opcao == 2:
    print(f'Você escolheu pagar a vista no dinheiro, então o desconto é de 5%, valor total: R${256 - (256 * 0.05)}')
elif opcao == 3:
    print('Preço normal: R$256')
elif opcao == 4:
     print(f'3x ou mais no cartão da 20% de juros, então o preço fica R${256 * 1.20}')
else:
    print(f'Essa opção não existe!')
