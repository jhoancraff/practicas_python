def run():
    numero = int(input('Elige un numero para mostrarte la tabla de multiplicar: '))
    for i in range(1, 11):
        print(f'{numero} * {i} = {i * numero}')


if __name__ == '__main__':
    run()