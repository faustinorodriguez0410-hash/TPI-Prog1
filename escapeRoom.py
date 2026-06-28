#Creo la funcion que maneja el ranking de jugadores
def guardarRanking (nombre, intentos):
    with open("rankingEscapeRoom.txt", "a") as archivo:
        archivo.write(f"Jugador: {nombre} - Total de intentos: {intentos}\n")