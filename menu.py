#Importacion de los modulos de juegos
import juego1
import juego2
import juego3
import juego4

#Creo la funcion que muestra el menú
def mostrarMenu():
    #Mensaje de bienvenida al usuario y opciones a elegir
    print("\n" + "*" * 30)
    print("   BIENVEIDOS A PLAYMATIC   ")
    print("*" * 30)
    print("1- Juego1")
    print("2- juego2")
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
            print("ERROR: Porfavor, ingrese un número valido (1 al 5).")

    opcion = int(opcion_str)