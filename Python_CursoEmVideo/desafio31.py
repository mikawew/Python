dist_viagem = float(input('Qual é a distância da sua viagem? '))

if dist_viagem < 200:
    valor_viagem_p = dist_viagem * 0.50
    print(f'A sua viagem de {dist_viagem}Km, custará R${valor_viagem_p:.2f}')
else:
    valor_viagem_m = dist_viagem * 0.45
    print(f'A sua viagem de {dist_viagem}Km, custará R${valor_viagem_m:.2f}')

print('Próximo passageiro... ')
