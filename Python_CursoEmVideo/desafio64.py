count = soma = 0

n1 = int(input('Digite o próximo valor: '))

while n1 != 999:
    count += 1
    soma += n1
    n1 = int(input('Digite o próximo valor: '))

print(f'Foram digitados {count} números. \n'
      f'E a soma entre eles foi: {soma}')
