from datetime import date
ano_bissexto = int(input('Digite um ano e direi se ele é bissexto (Coloque 0 para ano atual): '))

if ano_bissexto == 0:
    ano_bissexto = date.today().year

if ano_bissexto % 4 == 0 and ano_bissexto % 100 != 0 or ano_bissexto % 400 == 0:
    print(f'O ano {ano_bissexto:.0f} é bissexto')
else:
    print(f'O ano {ano_bissexto:.0f} é padrão')

print('Próximo ano...')

