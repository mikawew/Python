#

'''
    Aqui é aonde vai ter minhas revisões porém não irão estar salvas aq, mas na minha cabeça...

    len(nome) conta o número de caracteres

    count = normalmente pedimos para ele verificar quantas letras A tem em uma frase

    replace = consegue mudar uma palavra pela outra

    strip = remove os espaço de uma leitura em string

    slip = separa a frase em blocos 

    print(nome[1])

    upper = deixa em maiuscula

    lower = deixa em minuscula 

    in = por exemplo se eu quero achar algo, dentro de uma frase ('Aluno' in nome)

'''

nome = str(input('Digite o seu nome: ')).strip()

FirstName = nome.split()

print(f'Seu primeiro nome é {FirstName[0]}')

print(f'Seu último nome é: {FirstName[len(FirstName) - 1]}')




