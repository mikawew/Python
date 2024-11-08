from datetime import date

nasc = int(input('Digite o seu ano de nascimento: '))
idade = date.today().year - nasc

if idade <= 9:
    print('SUA CATEGORIA É MIRIM')

elif idade <= 14:
    print('SUA CATEGORIA É INFANTIL')

elif idade <= 19:
    print('SUA CATEGORIA É JUNIOR')

elif idade == 20:
    print('SUA CATEGORIA É SÊNIOR')

else:
    print('SUA CATEGORIA É MASTER')

