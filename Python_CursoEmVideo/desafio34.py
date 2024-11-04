sal = float(input('Digite o seu salário: R$'))

if sal > 1250:
    maior_sal = sal * 0.10
    novo_sal = sal + maior_sal
    print(f'Seu novo salário é R${novo_sal:.2f}')

else:
    men_sal = sal * 0.15
    novo_sal = sal + men_sal
    print(f'Seu novo salário é R${novo_sal:.2f}')

print()
print('Digite um novo salário...')

