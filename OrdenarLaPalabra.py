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
    palabras = ["python", "flask", "programacion", "matematica", "universidad"]
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