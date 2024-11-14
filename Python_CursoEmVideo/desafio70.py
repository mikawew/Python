soma = count = TotMil = menor_valor = 0
while True:
    produto = str(input('Digite o nome do produto: ')).strip()
    preco = float(input('Digite o preço do produto: R$'))

    #QUANTIDADE DE ITENS
    count += 1

    #TOTAL GASTO
    soma += preco

    #PRODUTOS > 1000
    if preco > 1000:
        TotMil += 1

    #CASO TENHA SÓ UM ITEM
    barato = ''
    if count == 1:
        menor_valor = preco
        barato = produto
    else:
        if preco < menor_valor:
            menor_valor = preco
            barato = produto
    #CASO TENHA MAIS DE UM

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break

print(f'O valor total gasto é R${soma:.2f}')
print(f'Temos {TotMil} produto(s) custando mais de R$1000.00')
print(f'Nome do item mais barato: {barato} que custa R${menor_valor:.2f}')
