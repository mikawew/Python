produtos = ('Sapatos', 125.50, 'Caderno', 13.50, 'Estojo', 5.80)

print('=' * 30)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('=' * 30)

for pos in range(0, len(produtos)):
    if pos % 2 == 0:
        print(f'{produtos[pos]:<30}', end='')
    else:
        print(f'R${produtos[pos]:>10.2f}')
