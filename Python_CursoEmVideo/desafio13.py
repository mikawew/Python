func = float(input('O seu salário atual é: R$'))

diferenca = func * (15 / 100)
novo_sal = func + diferenca

print(f'Seu salário teve um aumento de 15% entao vai para: R${novo_sal:.2f}')
