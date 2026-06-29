import random

# Ranking de jugadores (simple: guarda nombre y puntaje en memoria)
ranking = {}

def mostrarMenu():
    print("\n" + "=" * 40)
    print("   🎮 BIENVENIDO A ORDENAR LA PALABRA 🎮")
    print("=" * 40)
    print("1 - Jugar")
    print("2 - Ver Ranking")
    print("3 - Salir")
    print("=" * 40)

def jugar():
    nombre = input("Ingresa tu nombre: ")
    palabras = ["python", "flask", "programacion", "matematica", "universidad,"]
    palabra = random.choice(palabras)
    desordenada = "".join(random.sample(palabra, len(palabra)))

    print(f"\nLa palabra desordenada es: {desordenada}")
    intento = input("Ordena la palabra: ")

    if intento.lower() == palabra:
        print("✅ ¡Correcto! 🎉")
        # Suma puntos al ranking
        ranking[nombre] = ranking.get(nombre, 0) + 1
    else:
        print(f"❌ Incorrecto. La palabra era: {palabra}")
        
def verRanking():
    print("\n🏆 Ranking de jugadores 🏆")
    if not ranking:
        print("Todavía no hay jugadores en el ranking.")
    else:
        for jugador, puntaje in ranking.items():
            print(f"{jugador}: {puntaje} puntos")

def iniciarJuego():
    while True:
        mostrarMenu()
        opcion = input("Elige una opción: ")

        if opcion == "1":
            jugar()
        elif opcion == "2":
            verRanking()
        elif opcion == "3":
            print("👋 ¡Gracias por jugar! Hasta la próxima.")
            break
        else:
            print("⚠️ Opción inválida, intenta nuevamente.")