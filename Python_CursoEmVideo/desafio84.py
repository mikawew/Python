#LER NOME E PESO
pessoas = list()
dados = list()
num_maior = num_menor = 0
nome_maior = nome_menor = ''

while True:
    pessoas.append(str(input('Nome: ')))
    pessoas.append(int(input('Peso: ')))
    if len(dados) == 0:
        num_maior = num_menor = pessoas[1]
    else:
        if pessoas[1] > num_maior:
            num_maior = pessoas[1]
        if pessoas[1] < num_menor:
            num_menor = pessoas[1]

    dados.append(pessoas[:])
    pessoas.clear()

    resp = str(input('Quer continuar? '))
    if resp in 'Nn':
        break

print(f'Ao todo você cadastrou: {len(dados)} pessoas!')
print(f'O maior peso foi de {num_maior}Kg.')
print(f'O nome do maior peso: ', end='')
for p in dados:
    if p[1] == num_maior:
        print(f'{p[0]}')
print(f'O menor peso foi de {num_menor}Kg.')
print(f'O nome do(s) menor peso é: ', end='')
for p in dados:
    if p[1] == num_menor:
        print(f'{p[0]}', end='')
