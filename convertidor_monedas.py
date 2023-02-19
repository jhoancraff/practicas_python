def conversor(tipo_moneda, valor_dolar):

    moneda = input("¿Cuantos " + tipo_moneda + " tienes?: ")
    moneda = float(moneda)
    dolares = moneda / valor_dolar
    dolares = str(dolares)

    print("tienes $ " + dolares + " dolares")

menu = """
    Hola señor(a) usuario este es un conversor de moneda a dolar

    1 - Bolivares
    2 - Pesos colombianos
    3 - Pesos mexicanos
    4 - Pesos chileno

    Eliga una de las opciones: """

opcion = int(input(menu))

if opcion == 1:
    conversor("Bolivares ", 4.6)

elif opcion == 2:
    conversor("pesos colombianos ", 4000 )

elif opcion == 3:
    conversor("pesos mexicanos ", 21)

elif opcion == 4:
    conversor("pesos chilenos ", 804 )

else:
    print("Elige una de las 4 opciones")