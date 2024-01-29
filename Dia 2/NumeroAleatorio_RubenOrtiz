import random

def adivina_el_numero():
    # Seleccionar un número secreto aleatorio entre 1 y 100
    numero_secreto = random.randint(1, 100)
    attempts = 0

    print("¡Bienvenido al juego de adivinanza!")
    print("Intenta adivinar el número secreto entre 1 y 100. Tienes un total de 10 intentos.")

    while attempts < 10:
        try:
            adivina_el_usuario = int(input("\nIngresa tu suposición: "))

            if adivina_el_usuario < 1 or adivina_el_usuario > 100:
                print("Por favor, ingresa un número entre 1 y 100.")
                continue

            attempts += 1

            if adivina_el_usuario == numero_secreto:
                print(f"\n¡Felicidades! Has adivinado el número secreto {numero_secreto} en {attempts} intentos.")
                break
            elif adivina_el_usuario < numero_secreto:
                print("El número secreto es mayor. Intenta nuevamente.")
            else:
                print("El número secreto es menor. Intenta nuevamente.")

        except ValueError:
            print("Por favor, ingresa un número válido.")

    if attempts == 10:
        print(f"\nLo siento, has agotado tus 10 intentos. El número secreto era {numero_secreto}.")

if __name__ == "__main__":
    adivina_el_numero()