Tot18 = TotM = TotM20 = 0
while True:
    idade = int(input('Digite a sua idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if idade >= 18:
        Tot18 += 1
    if sexo == 'M':
        TotM += 1
    if sexo == 'F' and idade < 20:
        TotM20 += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break

print(f'Total de pessoas com mais de 18 anos: {Tot18}')
print(f'Ao todo temos {TotM} homens cadastrados! ')
