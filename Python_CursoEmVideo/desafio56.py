count_idade = 0
media_idade = 0
maior_idade = 0
nome_do_maior = ''
count_menor_20 = 0

for c in range (1, 5):
    nome = str(input(f'Digite o seu nome da {c}º pessoa: '))
    idade = int(input('Digite a sua idade: '))
    sexo = str(input('Digite o seu sexo "M" ou "F": ')).strip().upper()

    #MÉDIA DA IDADE
    count_idade += idade
    media_idade = count_idade / 4

    # HOMEM MAIS VELHO
    if c == 1 and sexo == 'M':
        maior_idade = idade
        nome_do_maior = nome
    else:
        if idade > maior_idade and sexo == 'M':
            maior_idade = idade
            nome_do_maior = nome

    #MULHERES TEM MENOS DE 20
    if sexo == 'F' and idade < 20:
        count_menor_20 += 1

print()
print(f'A idade média do grupo é {media_idade}')
print(f'O homem mais velho tem {maior_idade} anos e se chama: {nome_do_maior}')
print(f'Tem no total {count_menor_20} mulheres com menos de 20 anos.')
