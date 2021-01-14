num = int(input('Digite um número: '))
total = num
divisor = num - 1

print(f'O fatorial de {num} é:')
print(f'{num}!= 5', end='')

while divisor > 1:
    print(f'x{divisor}', end='')
    total *= divisor
    divisor -= 1

print(f' = {total}')
