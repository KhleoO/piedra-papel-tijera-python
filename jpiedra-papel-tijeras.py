nombre1 = input("Cómo se llamará el Jugador1?: ")
nombre2 = input("Cómo se llamará el Jugador2?: ")

jugador1 = input("Hola Jugador1! Qué eliges? Piedra, papel o tijera?: ")
jugador2 = input("Hola Jugador2! Qué eliges? Piedra, papel o tijera?: ")

condicion1 = jugador1 == "piedra" and jugador2 == "tijera"
condicion2 = jugador1 == "papel" and jugador2 == "piedra"
condicion3 = jugador1 == "tijeras" and jugador2 == "papel"

if jugador1 == jugador2:
    print("Ha sido un empate!")
elif condicion1 or condicion2 or condicion3:
    print("Ha ganado:", nombre1)
else:
    print("Ha ganado:", nombre2)

#---------------------------------------------------------------------------------------------

cant_intentos = 0
cant_max_intentos = 3
nombre1 = input("Cómo se llamará el Jugador1?: ")
nombre2 = input("Cómo se llamará el Jugador2?: ")
end_game = False

while not end_game:
    if not cant_intentos < cant_max_intentos:
        print("Se han terminado las oportunidades")
        break

    print("Hola,", nombre1,"!")
    jugador1 = input("Qué eliges? Piedra, papel o tijera?: ")
    minjugador1 = jugador1.lower()
    print("Hola,", nombre2,"!")
    jugador2 = input("Qué eliges? Piedra, papel o tijera?: ")
    minjugador2 = jugador2.lower()
    
    condicion1 = minjugador1 == "piedra" and minjugador2 == "tijera"
    condicion2 = minjugador1 == "papel" and minjugador2 == "piedra"
    condicion3 = minjugador1 == "tijera" and minjugador2 == "papel"
    
    if minjugador1 == minjugador2:
        print("Ha sido un empate!")
    elif condicion1 or condicion2 or condicion3:
        print("Ha ganado:", nombre1)
    else:
        print("Ha ganado:", nombre2)
    cant_intentos += 1
