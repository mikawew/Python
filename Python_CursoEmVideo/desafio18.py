import math

ang = float(input('Digite um ângulo: '))

sen = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tan = math.tan(math.radians(ang))

print(f'O cosseno do ângulo {ang} é: {cos:.2f}\n'
      f'O seno do ângulo é {sen:.2f}\n'
      f'O A tangente do ângulo é {tan:.2f}')

