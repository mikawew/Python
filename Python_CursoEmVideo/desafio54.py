from datetime import date

count_maioridade = 0
count_menor = 0

for c in range (1, 7+1):
    ano = int(input('Digite seu ano de nascimento: '))
    idade = date.today().year - ano

    if idade >= 18:
        count_maioridade += 1
    else:
        count_menor += 1

print(f'{count_menor} pessoas não atingiram a maioridade!')
print(f'{count_maioridade} pessoa atingiram a maioridade!')
