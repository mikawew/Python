n1 = float(input('Qual é a largura da parede? '))
n2 = float(input('Qual é a altura da parede? '))

area = n1 * n2
litros = area / 2
baldes = litros / 2

print(f'A parede tem dimensão de {n1}x{n2} e sua área é de {area}m²\n'
      f'Você irá precisar de {litros} litros de tinta.\n'
      f'Como cada bade tem 2 litros, você irá precisar de {baldes:.1f} balde(s) de tinta\n')

