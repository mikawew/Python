dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos Km rodados? '))

Tot_Dia = dias * 60
Tot_Km = km * 0.15

Total = Tot_Km + Tot_Dia

print(f'O total a pagar é de R${Total:.2f}')
