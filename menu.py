#Importacion de los modulos de juegos
import CulturaGeneral
import OrdenarLaPalabra
import juego3
import juego4

#Creo la funcion que muestra el menú
def mostrarMenu():
    #Mensaje de bienvenida al usuario y opciones a elegir
    print("\n" + "*" * 30)
    print("   BIENVEIDOS A PLAYMATIC   ")
    print("*" * 30)
    print("1- Juego1")
    print("2- Ordenar la Palabra")
    print("3- juego3")
    print("4- juego4")
    print("5. Salir")

#Creo la funcion que inicia el sistema (Maneja el bucle del menú y la seleccion de juegos)
def iniciarSistema():
    while True:
        mostrarMenu()
        opcion_str = input("Ingresa tu elección: ")
        #Valididación de datos para evitar errores si ingresan un numero no esperado
        if not opcion_str.isdigit():
            print("ERROR: Solo puede ingresar números, porfavor intente nuevamente.")

        opcion = int(opcion_str)
        #Estructura de seleccion de juegos/navegacion por el menú
        if opcion == 1:
            print("\n--- Iniciando Juego1 ---")
            CulturaGeneral.iniciarJuego()
        elif opcion == 2:
            print("\n--- Iniciando Juego2 ---")
            OrdenarLaPalabra.iniciarJuego()
        elif opcion == 3:
            print("\n--- Iniciando Juego3 ---")
            juego3.iniciarJuego()
        elif opcion == 4:
            print("\n--- Iniciando Juego4 ---")
            juego4.iniciarJuego()
        elif opcion == 5:
            print("\n--- ¡Gracias por jugar con nosotros!")
            break
        else: 
            print("\n Opción incorrecta: Por favor, elija un numero del 1 al 5")

#condicion verdadera para que iniciarSistema funcione directamente
if __name__ == "__main__":
    iniciarSistema