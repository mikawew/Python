valores_par = list()
valores_impar = list()
valores = list()

while True:
    valores.append(int(input('Digite um número: ')))
    resp = str(input('Deseja continuar? [S/N] '))
    if resp in 'Nn':
        break

for c, v in enumerate(valores):
    if v % 2 == 0:
        valores_par.append(v)
    elif v % 2 == 1:
        valores_impar.append(v)

print(f'Todos os números na lista: {valores}')
print(f'Número pares na lista: {valores_par}')
print(f'Número ímpares na lista {valores_impar}')

