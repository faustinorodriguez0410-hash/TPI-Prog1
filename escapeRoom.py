#Creo la funcion que maneja el ranking de jugadores
def guardarRanking (nombre, intentos):
    with open("rankingEscapeRoom.txt", "a") as archivo:
        archivo.write(f"Jugador: {nombre} - Total de intentos: {intentos}\n")

#Creo la funcion que contiene el juego
def jugarEscapeRoom():
    #Introducción y explicación del juego al usuario
    print("\n" + "=" * 30)
    print("  ESCAPE ROOM: EL LABORATORIO  ")
    print("=" * 30)

    nombre = input("Ingrese su nombre para comenzar a jugar: ")

    print(f"\n¡Atención {nombre}! ¡¡Te quedaste encerrado en el laboratorio de la UTN!!")
    print("Para conseguir la llave y salir, tenés que resolver 3 acertijos fáciles.")
    print("Si te equivocas, recibís una pista, pero sumás intentos. ¡Intenta salir con los menores intentos posibles!\n")

    #para la estrucuta de datos voy a usar tuplas que contienen (Acertijo, respuesta, pista)
    
    acertijos = [("Tengo agujas pero no sé coser, tengo números pero no sé sumar. ¿Qué soy?", "reloj", "Pista: Hace 'tic tac'."),
                 ("Vuelo sin alas, lloro sin ojos. ¿Qué soy?", "nube", "Pista: Está en el cielo y tapa el Sol."),
                 ("Soy alta cuando soy joven, y baja cuando soy vieja. ¿Qué soy?", "vela", "Pista: Se usa cuando se corta la luz y da fuego.")
                 ]

    intentosTotales = 0

    numero = 1
    for acertijo in acertijos:
        # Desempaquetamos los elementos de la tupla
        pregunta = acertijo[0]
        respuesta_correcta = acertijo[1]
        pista = acertijo[2]
        
        print(f"--- Acertijo {numero} ---")
        print(pregunta)
        
        resuelto = False

        #Ciclo que obliga a resolver el acertijo para poder continuar con el siguiente
        while not resuelto:
            intentosTotales += 1
            # Se limpia la entrada para evitar errores si el usuario pone espacios extra o mayúsculas
            respuesta_usuario = input("Tu respuesta: ").lower().strip()
            
            #Validacion de la respuesta
            if respuesta_usuario == respuesta_correcta:
                print("¡Correcto! Has descifrado este acertijo.\n")
                resuelto = True
            else:
                print(f"Respuesta incorrecta. {pista}")
                print("Inténtalo de nuevo...\n")
        numero += 1
                
    print(" ¡Felicidades! Resolviste todos los acertijos, encontraste la llave y lograste salir del laboratorio.")
    print(f"Total de intentos utilizados: {intentosTotales}")
    
    guardarRanking(nombre, intentosTotales)

def iniciarJuego():
    """Punto de entrada del juego 4, utilizado en el menu.py."""
    jugarEscapeRoom()