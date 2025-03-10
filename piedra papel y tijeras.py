import random
import getpass

def obtener_opcion(mensaje="Elige una opción (1: Piedra, 2: Papel, 3: Tijeras): ", ocultar=False):
    opciones = {"1": "Piedra", "2": "Papel", "3": "Tijeras"}
    while True:
        opcion = getpass.getpass(mensaje) if ocultar else input(mensaje)
        if opcion in opciones:
            return opciones[opcion]
        print("Opción inválida, intenta de nuevo.")

def determinar_ganador(opcion1, opcion2):
    reglas = {"Piedra": "Tijeras", "Papel": "Piedra", "Tijeras": "Papel"}
    if opcion1 == opcion2:
        return "Empate"
    return "Jugador 1 gana" if reglas[opcion1] == opcion2 else "Jugador 2 gana"

def jugar_contra_computadora():
    global ultima_partida
    print("\n--- Jugar contra la computadora ---")
    opcion_jugador = obtener_opcion()
    opcion_computadora = random.choice(["Piedra", "Papel", "Tijeras"])
    print(f"Computadora eligió: {opcion_computadora}")
    resultado = determinar_ganador(opcion_jugador, opcion_computadora)
    print(f"Resultado: {resultado}\n")
    ultima_partida = ("Computadora", opcion_jugador, opcion_computadora, resultado)

def jugar_multijugador():
    global ultima_partida
    print("\n--- Jugar multijugador ---")
    opcion_jugador1 = obtener_opcion("Jugador 1, ingresa tu opción: ", ocultar=True)
    opcion_jugador2 = obtener_opcion("Jugador 2, ingresa tu opción: ", ocultar=True)
    resultado = determinar_ganador(opcion_jugador1, opcion_jugador2)
    print(f"\nResultado: {resultado}\n")
    ultima_partida = ("Multijugador", opcion_jugador1, opcion_jugador2, resultado)

def ver_estadisticas():
    if ultima_partida is None:
        print("\nNo hay estadísticas disponibles. Juega una partida primero.\n")
    else:
        print("\n--- Estadísticas de la última partida ---")
        modo, opcion1, opcion2, resultado = ultima_partida
        print(f"Modo de juego: {modo}")
        print(f"Jugador 1 eligió: {opcion1}")
        print(f"Jugador 2/Computadora eligió: {opcion2}")
        print(f"Resultado: {resultado}\n")

def menu():
    global ultima_partida
    ultima_partida = None
    while True:
        print("--- Menú Principal ---")
        print("1. Jugar contra la computadora")
        print("2. Jugar multijugador")
        print("3. Ver estadísticas de la última partida")
        print("4. Salir")
        opcion = input("Elige una opción: ")
        opciones_menu = {"1": jugar_contra_computadora, "2": jugar_multijugador, "3": ver_estadisticas}
        if opcion in opciones_menu:
            opciones_menu[opcion]()
        elif opcion == "4":
            print("Saliendo del juego. ¡Hasta la próxima!")
            break
        else:
            print("Opción inválida, intenta de nuevo.\n")

menu()
