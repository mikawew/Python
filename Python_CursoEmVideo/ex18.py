pessoas = list()
dados = ['Pedro', 25]

pessoas.append(dados[:])
# O [:] faz um fatiamento
"""Faz com que a lista 'dados'(tem 0 (Pedro) e tem o 1(25)  ) fique dentro da lista 'pessoas' (0)"""

#É possível também fazer isso:
nomes = ['Pedro', 25], ['Maria', 19], ['João', 32]

print(nomes[0][0])
print(nomes[1][1])
