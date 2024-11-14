soma = count = 0

while count != 999:
    count = int(input('Digite um número: '))
    if count == 999:
        break
    soma += count
print(f'A soma entre eles: {soma}')
