ficha = list()

while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 1: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    resp = str(input('Quer continuar? [S/N]'))
    if resp in 'Nn':
        break

print('=' * 30)
print(f'{"No.":<4}{"Nome":<10}{"MEDIA":>8}')

for i, a in enumerate(ficha):
    print(f'{i+1:<4}{a[0]:<10}{a[2]:>8.1f}')

while True:
    print('=' * 30)
    opc = int(input('Mostras as notas de qual aluno? (9999 interrompe): '))
    if opc == 9999:
        print('FINALIZANDO')
        break
    if opc <= len(ficha) - 1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
print('VOLTE SEMPRE')
