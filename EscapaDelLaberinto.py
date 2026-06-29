ranking = {}

def mostrarMenu():
    print("\n" + "=" * 40)
    print("   🌀 BIENVENIDO A ESCAPE DEL LABERINTO 🌀")
    print("=" * 40)
    print("1 - Jugar")
    print("2 - Ver Ranking")
    print("3 - Salir")
    print("=" * 40)

def jugar():
    nombre = input("Ingresa tu nombre: ")
    puntaje = 0

    # Representación del laberinto (X = pared, S = salida, . = camino)
    laberinto = [
        ["X","X","X","X","X"],
        ["X",".",".",".","X"],
        ["X",".","X",".","X"],
        ["X",".","X","S","X"],
        ["X","X","X","X","X"]
    ]

    pos = [1,1]  # posición inicial

    print("\nEstás dentro del laberinto. Usa N/S/E/O para moverte, Q para salir.")

    while True:
        print(f"Tu posición actual: {pos}")
        movimiento = input("Mover (N/S/E/O/Q): ").upper()

        if movimiento == "Q":
            print("👋 Saliste del juego.")
            break

        nueva_pos = pos.copy()
        if movimiento == "N": nueva_pos[0] -= 1
        elif movimiento == "S": nueva_pos[0] += 1
        elif movimiento == "E": nueva_pos[1] += 1
        elif movimiento == "O": nueva_pos[1] -= 1
        else:
            print("⚠️ Movimiento inválido.")
            continue

        if laberinto[nueva_pos[0]][nueva_pos[1]] == "X":
            print("🚧 Chocaste contra una pared.")
        elif laberinto[nueva_pos[0]][nueva_pos[1]] == "S":
            print("🎉 ¡Encontraste la salida!")
            puntaje += 10
            print(f"🏆 {nombre}, tu puntaje final es: {puntaje}")
            ranking[nombre] = ranking.get(nombre, 0) + puntaje
            break
        else:
            pos = nueva_pos
            print("➡️ Te moviste con éxito.")