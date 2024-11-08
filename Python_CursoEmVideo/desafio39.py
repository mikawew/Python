from datetime import date

nasc = int(input('Em que ano que você nasceu? '))

idade = date.today().year - nasc

if idade == 18:
    print(f'Como você tem {idade}, você tem quer se alistar ao serviço militar.')

elif idade > 18:
    passou = idade - 18
    print(f'Ja passou {passou} ano(s) do alistamento militar. ')

else:
    falta = 18 - idade
    print(f'Falta para você {falta} ano(s) para o alistamento militar')

