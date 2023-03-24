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

""""
La condicion 1 es que se pueda jugar contra la maquina
La condicion 2 es que se pueda mostrar quien gana
La condicion 3 es que se pueda repetir el juego
La condicion 4 es que se usen  funciones en su desarrollo
La condicion 5 es que se haga uso de vectores (array)

"""

class juegoPPT:

    def __init__(self) :
        self.opciones= ["piedra", "papel", "tijeras"]

    def jugar(self):
        while True:
            self.user()
            print(WHITE)
            repetir = input ("Escribe 'S' para volver a JUGAR o 'N' para TERMINAR: ").lower()
            if repetir != "s":
                print(RED)
                print("GAME OVER")
                print(RESET)
                break
        print(RESET) 

    def user(self):
    #input user
        print(BLUE)
        opcion_usuario = input("Piensa y Escribe una de estas opciones: \n Piedra \n Papel \n Tijeras \n \n").lower()
        print(RESET)
        print(GREEN)
        print("El HUMANO escribio: \n",opcion_usuario)
        print(RESET)
    #option machine
        print(CYAN)
        option_machine = random.choice(self.opciones)
        print("La MAQUINA escribio: \n",option_machine)
        print(RESET)
        print(RED)
        if  opcion_usuario not in self.opciones:
            print ("Opcion No Valida \nIntenta De Nuevo \n")
            self.user()
            print(RESET)
        else:
            self.compare(option_machine, opcion_usuario)

    #Reglas
    print(RED)
    def compare (pc, player, self):
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

juego = juegoPPT()
juego.jugar()
