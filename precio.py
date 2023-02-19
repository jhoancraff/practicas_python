def run():

    menu = """
        Hola señor usuario aqui tenemos una lista de precios:

            1 - harina
            2 - arroz
            3 - azucar
            4 - caraota
            5 - jabón
            6 - carne
            7 - pollo

        elige una opciones: """

    opcion = input(menu)

    if opcion == 'harina':
        print('la harina cuesta 4000')
    elif opcion == 'arroz' :
        print('el arroz cuesta 2500')
    elif opcion == 'azucar':
        print('la azucar cuesta 3500')
    elif opcion == 'caraota':
        print('las caraota cuesta 7000')
    elif opcion == 'jabon':
        print('el jabon cuesta 1500')
    elif opcion == 'carne':
        print('la carne cuesta 16000')
    elif opcion == 'pollo':
        print('el pollo cuesta 23000')

if __name__ == '__main__':
    run()