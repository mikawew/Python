valores = list()

while True:
    n = int(input('Digite um valor: '))
    if n not in valores:
        valores.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado')

    r = str(input('Quer continuar? [S/N] '))
    if r in 'Nn':
        break

print(f'Você digitou os valores {sorted(valores)}')

