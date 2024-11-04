vel_carro = float(input('Em que velocidade o carro estava? '))

if vel_carro > 80:
    rest_vel = vel_carro - 80
    pag_multa = rest_vel * 7.0
    print(f'O dono pagará uma multa ao total de R${pag_multa:.2f}, por ter passado a {rest_vel:.0f}Km/h da velocidade da via!')
else:
    print('O dono não deve pagar nada!')

print('Próximo carro...')
