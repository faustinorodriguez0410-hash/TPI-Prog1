def guardarRanking(nombre, puntaje):
    """Guarda el puntaje en un archivo de texto."""
    with open("rankingCultura.txt", "a") as archivo:
        archivo.write(f"Jugador: {nombre} - Puntaje: {puntaje} puntos\n")
# Función principal del juego de Cultura General
def cultura_general():
    """Lógica principal del juego."""
    # Lista que contiene las preguntas, las opciones y la respuesta correcta
    preguntas = [
        {"pregunta": "¿Cuál es el planeta más grande del Sistema Solar?", "opciones": ["Marte", "Júpiter", "Venus", "Saturno"], "respuesta": 2},
        {"pregunta": "¿Cuántos continentes hay en el mundo?", "opciones": ["5", "6", "7", "8"], "respuesta": 2},
        {"pregunta": "¿Quién pintó la Mona Lisa?", "opciones": ["Pablo Picasso", "Leonardo da Vinci", "Vincent van Gogh", "Miguel Ángel"], "respuesta": 2},
        {"pregunta": "¿Cuál es la capital de Argentina?", "opciones": ["Rosario", "Córdoba", "Buenos Aires", "Mendoza"], "respuesta": 3},
        {"pregunta": "¿Qué océano es el más grande del planeta?", "opciones": ["Atlántico", "Índico", "Pacífico", "Ártico"], "respuesta": 3}
    ]
     # Variable donde se acumula el puntaje
    puntaje = 0

    print("\n--- ¡A JUGAR! ---")
     # Recorre todas las preguntas de la lista
    for i, p in enumerate(preguntas, start=1):
        print(f"\nPregunta {i}: {p['pregunta']}")
         # Muestra las opciones de respuesta
        for j, op in enumerate(p['opciones'], start=1):
            print(f"{j}. {op}")
        # Valida que el usuario ingrese un número entre 1 y 4
        while True:
            try:
                resp = int(input("Ingrese su respuesta (1-4): "))
                if 1 <= resp <= 4:
                    break
                print("Debe ingresar un número entre 1 y 4.")
            except ValueError:
                print("Ingrese un número válido.")
        # Verifica si la respuesta es correcta 
        if resp == p['respuesta']:
            print("¡Correcto!")
            puntaje += 20
        else:
            print(f"Incorrecto. La respuesta era: {p['opciones'][p['respuesta']-1]}")
         # Muestra el resultado fina
    print(f"\nPuntaje final: {puntaje} de 100")
    # Solicita el nombre del jugador
    nombre = input("Ingrese su nombre para el ranking: ")
     # Guarda el nombre y el puntaje en el archivo ranking.txt
    guardarRanking(nombre, puntaje)

def verRanking():
    """Muestra el ranking desde el archivo de texto."""
    print("\n🏆 Ranking de Cultura General 🏆")
    try:    
        with open("rankingCultura.txt", "r") as archivo:
            lineas = archivo.readlines()
            if not lineas:
                print("Todavía no hay jugadores.")
            else:
                for linea in lineas:
                    print(linea.strip())
    except FileNotFoundError:
        print("Todavía no hay jugadores registrados.")

def mostrarMenu():
    print("\n" + "=" * 40)
    print(" 🎮 BIENVENIDO A CULTURA GENERAL 🎮")
    print("=" * 40)
    print("1 - Jugar")
    print("2 - Ver Ranking")
    print("3 - Volver al Menú Principal")
    print("=" * 40)
# Solicita al usuario que escriba el comando para iniciar el juego
def iniciarJuego():
    """Función que llama el menu.py"""
    while True:
        mostrarMenu()
        opcion = input("Elige una opción: ")
        if opcion == "1":
            cultura_general()
        elif opcion == "2":
            verRanking()
        elif opcion == "3":
            break
        else:
            print("⚠️ Opción inválida.")