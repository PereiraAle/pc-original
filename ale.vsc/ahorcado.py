import random

def jugar_ahorcado():
    palabras = ["tini", "chano", "bondiola", "criminalistica", "pochita", "roma cuzzolino pereira", "cuzzolino","17 meses", "mini pochi"]
    palabra = random.choice(palabras)
    letras_adivinadas = []
    intentos = 7

    while intentos > 0:
        palabra_mostrada = ""
        for letra in palabra:
            if letra in letras_adivinadas:
                palabra_mostrada += letra + " "
            else:
                palabra_mostrada += "_ "

        print("Palabra:", palabra_mostrada)
        print("Intentos restantes:", intentos)

        if palabra_mostrada.replace(" ", "") == palabra:
            print("¡Ganastee!")
            return

        letra_ingresada = input("Ingresa una letra: ").lower()

        if letra_ingresada in letras_adivinadas:
            print("Ya ingresaste esa letra. ¡Intenta otravez!")
        elif letra_ingresada in palabra:
            print("Le pegaste, adivinaste una letra")
            letras_adivinadas.append(letra_ingresada)
        else:
            print("¡Le erraste! perdiste un intento.")
            intentos -= 1
            letras_adivinadas.append(letra_ingresada)

    print("¡Perdiste! La palabra correcta era:", palabra)

jugar_ahorcado()
