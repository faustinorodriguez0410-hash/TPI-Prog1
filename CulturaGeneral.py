# Función principal del juego de Cultura General
def cultura_general():

    # Lista que contiene las preguntas, las opciones y la respuesta correcta
    preguntas = [
        {
            "pregunta": "¿Cuál es el planeta más grande del Sistema Solar?",
            "opciones": ["Marte", "Júpiter", "Venus", "Saturno"],
            "respuesta": 2
        },
        {
            "pregunta": "¿Cuántos continentes hay en el mundo?",
            "opciones": ["5", "6", "7", "8"],
            "respuesta": 3
        },
        {
            "pregunta": "¿Quién pintó la Mona Lisa?",
            "opciones": ["Pablo Picasso", "Leonardo da Vinci", "Vincent van Gogh", "Miguel Ángel"],
            "respuesta": 2
        },
        {
            "pregunta": "¿Cuál es la capital de Argentina?",
            "opciones": ["Rosario", "Córdoba", "Buenos Aires", "Mendoza"],
            "respuesta": 3
        },
        {
            "pregunta": "¿Qué océano es el más grande del planeta?",
            "opciones": ["Atlántico", "Índico", "Pacífico", "Ártico"],
            "respuesta": 3
        }
    ]
    # Variable donde se acumula el puntaje
    puntaje = 0

    print("\n===================================")
    print("      CULTURA GENERAL")
    print("===================================")

    # Recorre todas las preguntas de la lista
    for i, pregunta in enumerate(preguntas, start=1):

        print(f"\nPregunta {i}")
        print(pregunta["pregunta"])
         # Muestra las opciones de respuesta
        for j, opcion in enumerate(pregunta["opciones"], start=1):
            print(f"{j}. {opcion}")

        # Valida que el usuario ingrese un número entre 1 y 4
        while True:
            try:
                respuesta = int(input("Ingrese su respuesta (1-4): "))

                if 1 <= respuesta <= 4:
                    break
                else:
                    print("Debe ingresar un número entre 1 y 4.")

            except ValueError:
                print("Ingrese un número válido.")

        # Verifica si la respuesta es correcta
        if respuesta == pregunta["respuesta"]:
            print("¡Correcto!")
            puntaje += 20

        else:
            correcta = pregunta["opciones"][pregunta["respuesta"] - 1]
            print(f"Incorrecto. La respuesta correcta era: {correcta}")

    # Muestra el resultado final
    print("\n===================================")
    print("           RESULTADO")
    print("===================================")
    print(f"Puntaje final: {puntaje} de 100")

    # Solicita el nombre del jugador
    nombre = input("Ingrese su nombre: ")

    # Guarda el nombre y el puntaje en el archivo ranking.txt
    archivo = open("ranking.txt", "a")
    archivo.write(nombre + " - " + str(puntaje) + " puntos\n")
    archivo.close()

    print("¡Puntaje guardado correctamente!")