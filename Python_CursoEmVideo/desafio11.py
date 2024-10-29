from traceback import print_tb

n1 = float(input('Qual é a largura da parede? '))
n2 = float(input('Qual é a altura da parede? '))

area = n1 * n2
litros = area / 2
baldes = litros / 2

print(f'Você irá precisar de {litros} litros de tinta.\n'
      f'você irá precisar de {baldes} baldes de tinta')
