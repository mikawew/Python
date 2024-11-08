valor_casa = float(input('Qual o valor da casa? R$'))
sal = float(input('Qual o valor do seu salário? R$'))

ano = int(input('Em quantos anos pretende pagar?'))

pagam_mensal = valor_casa / (ano * 12)
minimo = sal * 30 / 100

print(f'Para pagar uma casa de R${valor_casa:.2f} em {ano} anos ', end='')
print(f'a prestação da casa será de: R${pagam_mensal:.2f}')

if pagam_mensal <= minimo:
    print('SEU EMPRÉSTIMO FOI ACEITO')

else:
    print('SEU EMPRÉSTIMO FOI CANCELADO, ', end='')
    print('ACABOU EXERCENDO MAIS DE 30% DO SEU SALÁRIO')



