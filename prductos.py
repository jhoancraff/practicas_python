def run():
    menu = """
        Hola este programa te da los precios de estos producto:

        1 - Harina
        2 - Azucar
        3 - Aceite
        4 - Cafe
    
    Elige una de estas opciones: """
                                                                                                                                                        
    opcion = int(input(menu))

    if opcion == 1:
        print("4000")
    
    elif opcion == 2:
        print("2000")

    elif opcion == 3:
        print("7000")

    elif opcion == 4:
        print("3000")

    else:
        print("Eliga una opcion correcta")        


if __name__ == "__main__":
    run()