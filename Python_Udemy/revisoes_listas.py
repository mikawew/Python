'''
não é possível fazer shortcut com a variável list:
valores_par = valores = list()

As listas não são imutáveis

lanche = ['hamburguer', 'pizza', 'suco', 'sorvete']

(ADICIONANDO)
lanche.append('biscoito') <- utilizado para adicionar no final da lista
lanche.inser(0, 'hotdog') <- insere hotdog na primeira ordem da lista
lanche.append(int(input('Digite um valor: ))) <- é possível juntar

(ELIMINANDO)
del lanche[3]
lanche.pop(3)
lanche.pop() <- elimina o último elemento
lanche.remove('pizza') <- elimina o elemento e elimina o valor

(CRIAÇÃO)
valores = list(range(4,11)) <- uma função de lista 

(ORDEM REVERSA)
valores.sort(reverse=True) <- coloca valores em ordem decrescente

(LIGAÇÃO)
b = a[:] <- Não há ligação desse jeito
'''
