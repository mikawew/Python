n = input('Digite algo: ')

print('O tipo primitivo desse valor é ', type(n))
print('É um alfabético? ', n.isalpha())
print('É decimal? ', n.isdecimal())
print('Ele está em maiúscula? ', n.isupper())
print('Só tem espaço? ', n.isspace())
print('É um número? ', n.isnumeric())
print('É um alfanumérico? ', n.isalnum())
