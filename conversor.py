def conversor(tipo_peso, valor_dolar):
    pesos = float(input("cuantos pesos " + tipo_peso + " tienes?: "))
    dolares = pesos / valor_dolar
    dolares = round(dolares,2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dolares")



menu = """
Bienvenido al conversor de monedas 👍

1.- Pesos colombianos
2.- Pesos argentinos
3.- Pesos mexicanos

Elige una opcion: """

opcion = int(input(menu))

if opcion == 1:
    conversor("colombianos", 3875)
    # pesos = float(input("Cuántos pesos colombianos tienes: "))
    # valor_dolar = 3450
    # dolares = pesos / valor_dolar
    # dolares = round(dolares,2)
    # dolares = str(dolares)
    # print("Tienes $" + dolares + " dólares")
elif opcion == 2:
    conversor("argentinos", 65)
elif opcion == 3:
    conversor("mexicanos", 24)
else:
    print('Ingresa una opcion correcta por favor')






