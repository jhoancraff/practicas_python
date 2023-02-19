def run():
    contador_externo = 0
    contado_interno = 0

    while contador_externo < 5:
        while contado_interno < 6:
            print(contador_externo, contado_interno)
            contado_interno += 1
                
        contador_externo += 1
        contado_interno = 0


if __name__ == '__main__':
    run()