'''
As tuplas são variáveis compostas e imutáveis que permitem armazenar vários valores em uma mesma estrutura, acessíveis, por chaves individuais.

print(sorted(lanche)) <- Ele coloca a tupla em ordem alfabética

é possível fazer a junção de tuplas utilizando + entre elas

propriedade index mostra a posição da tupla, caso tenha 2

é possível juntar números com strings em tuplas

count = (5, 89, 2, 3, 4, 5, 7)
Ex: print(count.index(5, 1)) <- o número 5 é a posição aonde será mostrada, já o 1 é a quantidade de deslocamento daquele número, no caso começará no 1(89) e não no 0(5), com isso é possível verificar 2 números repetidos na mesma tupla.

com del() é possível apagar variáveis

propriedade max() e min()

possibilidade de colocar variáveis dentro da tupla

'''


lanche = ('HAMBURGUER', 'SODA', 'GUÁRANA')
# ou lanche = 'HAMBURGUER', 'SODA', 'GUÁRANA'

print(lanche)

for comida in lanche:
    print(f'O senhor pediu {comida}')

for pos, food in enumerate(lanche):
    print(f'Eu vou comer {food} na posição {pos+1}')
