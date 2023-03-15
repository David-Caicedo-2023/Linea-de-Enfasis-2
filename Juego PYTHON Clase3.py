BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[39m' '\033[30m'

import random

#Necesitamos crear con phyton un juego clasico de piedra, papel o tijeras que cumpla con:

""""
La condicion 1 es que se pueda jugar contra la maquina
La condicion 2 es que se pueda mostrar quien gana
La condicion 3 es que se pueda repetir el juego
La condicion 4 es que se usen  funciones en su desarrollo
La condicion 5 es que se haga uso de vectores (array)

"""

print("Juego piedra, papel o tijeras \n _____________________ \n")

#Array
options = ["piedra", "papel", "tijeras"]

def user():
#input user
    print(BLUE)
    optionUser = input("Piensa y Escribe una de estas opciones: \n Piedra \n Papel \n Tijeras \n \n").lower()
    print(RESET)
    print(GREEN)
    print("El HUMANO escribio: \n",optionUser)
    print(RESET)
#option machine
    print(CYAN)
    option_machine = random.choice(options)
    print("La MAQUINA escribio: \n",option_machine)
    print(RESET)

    print(RED)
    if optionUser not in options:
        print ("Opcion No Valida \nIntenta De Nuevo \n")
        user()
        print(RESET)
    else:
        compare(option_machine, optionUser)


#Reglas
print(RED)
def compare (pc,player):
    #Empate!!
    if pc == player:
        print ("Empate!!")
    elif pc == "piedra" and player == "tijeras":
        print ("Gano: MAQUINA ---- Perdio: HUMANO")
    elif pc == "papel" and player == "piedra":
        print ("Gano: MAQUINA ---- Perdio: HUMANO")
    elif pc == "tijeras" and player == "papel":
        print ("Gano: MAQUINA ---- Perdio: HUMANO")
    else:
        print("Gano: HUMANO ---- Perdio: MAQUINA")
    print(RESET)

def jugar():
    while True:
        user()
        print(WHITE)
        repetir = input ("Escribe 'S' para volver a JUGAR o 'N' para TERMINAR: ").lower()
        if repetir != "s":
            print(RED)
            print("GAME OVER")
            print(RESET)
            break
        print(RESET)

jugar()
