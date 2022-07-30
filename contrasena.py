import random



def generador_contrasena():
    mayusculas = ['A', 'B']
    minusculas = ['a', 'b']
    simbolos = ['!', '@']
    numeros = ['1','2']

    contrasena = mayusculas + minusculas + simbolos + numeros

    contrasena = []

    for i in range (8):
        caracter_random = random.choice(caracteres )
        contrasena.append(caracter_random)

    contrasena = "".join(contrasena)
    return contrasena


def run():
    contrasena = generador_contrasena()
    print('Tu nueva contrasena es: ' + contrasena)


if __name__ == '__menu__':
    run()