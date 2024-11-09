stotal = 0
s = 0
for c in range (1, 6+1):
    n1 = int(input(f'Digite o {c}º número aqui: '))
    stotal += n1
    if n1 % 2 == 0:
        s += n1
print(f'A soma dos números pares é: {s}\n'
      f'Caso queria o valor total: {stotal}')
