saque = int(input('Quantos reais deseja sacar? '))
cedulas_cinquenta = cedulas_vinte = cedulas_dez = cedulas_um = 0

while True:
    if saque >= 50:
        cedulas_cinquenta += 1
        saque -= 50
    if saque >= 20 and saque < 50:
        cedulas_vinte += 1
        saque -= 20
    if saque >= 10 and saque < 20:
        cedulas_dez += 1
        saque -= 10
    if saque >= 1 and saque < 10:
        cedulas_um += 1
        saque -= 1
    if saque == 0:
        break

print('Total de:')
if cedulas_cinquenta > 0:
    print(f'{cedulas_cinquenta} cédulas de R$50')
if cedulas_vinte > 0: 
    print(f'{cedulas_vinte} cédulas de R$20')
if cedulas_dez > 0:
    print(f'{cedulas_dez} cédulas de R$10')
if cedulas_um > 0:
    print(f'{cedulas_um} cédulas de R$1')
