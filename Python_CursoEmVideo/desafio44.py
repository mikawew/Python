produto = float(input('Qual o valor do produto? R$'))
print('''Selecione o método de pagamento:
[1] À vista dinheiro ou cheque com 10% de desconto
[2] À vista no cartão 5% de desconto
[3] Em até 2x no cartão (preço normal), mais de 3x (juros de 20%):
''')
cond_pag = int(input('Qual a condição do pagamento? '))

#À vista dinheiro/cheque 10% de desconto
if cond_pag == 1:
    desconto_produto = produto * 10 / 100
    valor_produto = produto - desconto_produto
    print(f'O valor do produto à VISTA NO DINHEIRO ficou R${valor_produto:.2f}')

#À vista cartão 5% de desconto
elif cond_pag == 2:
    desconto_produto = produto * 5 / 100
    valor_produto = produto - desconto_produto
    print(f'O valor do produto à VISTA NO CARTÃO ficou R${valor_produto:.2f}')

#2x no cartao preço normal
elif cond_pag == 3:
    parcelas = int(input('Em quantas parcelas deseja pagar? '))
    if parcelas == 2:
        print(f'Seu produto vai ser pago em 2x no cartão ficando: R${produto / parcelas:.2f} por mês.')

    else:
        juros_produto = produto * 20 / 100
        valor_produto = juros_produto + produto
        print(f'O valor total do produto ficou R${valor_produto:.2f} e ficou {parcelas}x no cartão ficando por mês {valor_produto / parcelas:.2f}')
#3x ou mais no cartao 20% de juros
else:
    print('Digitou valor errado...')

