n1 = float(input('Qual é o preço do produto? R$'))

Qtd_Desconto = int(input('Quanto de desconto você quer oferecer? '))

conta = n1 * (Qtd_Desconto / 100)
desconto = n1 - conta

print(f'O mesmo produto com {Qtd_Desconto}% de desconto fica: R${desconto:.2f}')


