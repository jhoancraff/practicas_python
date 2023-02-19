from __future__ import division


def run():
    print(f'Hola señor usuario vamos a ver si un numero es par o impar')
    numero = int(input('Escoge un numero: '))

    
    while True:
        if numero%2 == 0:
                    print('Es par ')
        
        elif numero%2 != 0:
                
                print('No es par ')
        
        numero2 = int(input('Elige otro numero: '))
        numero = numero2
                                                                     


if __name__ == '__main__':
    run()