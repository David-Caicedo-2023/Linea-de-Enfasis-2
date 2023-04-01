""""
Un estudio de ciencias  de la salud fisica ha determinado  una secuencia de habitos
que favorecen a la recuperacion de energia y otros que  no benefician y producen perdida 
de energia.
Se solicita crear una APP en phyton que permita determinar la energia total del usuario
segun las siguientes condiciones:

1. Toda persona debe tener minimo como 40  de energia para sobrevivir.
2. Sobre pasar de 250 de energia, puede causar la muerte.
   (El sistema debera anunciar el peligro).
3. Se recupera energia con:
*   Comer sano: 30 energia.
*   Dormir 8 horas: 100 energia.
*   Comer sin restricciones: 75 energia.
4. Se pierde energia con:
*   Correr: -20 energia.
*   Ver Tv: -5 energia.
*   Caminar: -10 energia.
5. Toda persona inicia el APP afirmando en las options una accion a ejecutar.
6. Busque controlar que todos los datos sean correctos

"""
#Colores

BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[39m' '\033[30m'

#Opciones 
options = ["Comer Sano", "Dormir", "Comer Sin Restricciones", "Correr", "Ver Tv", "Caminar"]

#Clase Principal
class Persona:
    def __init__(self,nombre,fecha_nac,cedula):
        self.nombre = nombre
        self.fecha_nac = fecha_nac
        self.cedula = cedula
        self.nivel_energia = energia = 80

#Funciones
    def comerSano(self):
        print(f"{self.nombre} esta comiendo sano")
        self.nivel_energia +=30
        if self.nivel_energia == 249:
            print()
            print(RED)
            print(f"{self.nombre} tienes la energia en ({self.nivel_energia}) y has muerto por que has excedido el nivel de energia maximo (250)\n")
            print("GAME OVER")
            print(RESET)
            print()
            exit()
        elif self.nivel_energia > 249:
            print()
            print(RED)
            print(f"{self.nombre} tienes la energia en ({self.nivel_energia}) y has muerto por que has excedido el nivel de energia maximo (250)\n")
            print("GAME OVER")
            print(RESET)
            print()
            exit()
        elif self.nivel_energia >= 180:
            print()
            print(MAGENTA)
            print(f"{self.nombre} tienes una energia de" ,{self.nivel_energia}, "esta por encima de la energia normal el maximo es (250)\nsi se excede se podria desmayar o podria morir\n")
            print(RESET)
        else:
            print("Tu nivel de energia actual  es: ", self.nivel_energia, "\n")
    def dormir(self):
        print(f"{self.nombre} esta durmiendo", self.nivel_energia)
        self.nivel_energia +=100
        if self.nivel_energia == 249:
            print()
            print(RED)
            print(f"{self.nombre} tienes la energia en ({self.nivel_energia}) y has muerto por que has excedido el nivel de energia maximo (250)\n")
            print("GAME OVER")
            print(RESET)
            print()
            exit()
        elif self.nivel_energia > 249:
            print()
            print(RED)
            print(f"{self.nombre} tienes la energia en ({self.nivel_energia}) y has muerto por que has excedido el nivel de energia maximo (250)\n")
            print("GAME OVER")
            print(RESET)
            print()
            exit()
        elif self.nivel_energia >= 180:
            print()
            print(MAGENTA)
            print(f"{self.nombre} tienes una energia de" ,{self.nivel_energia}, "esta por encima de la energia normal el maximo es (250)\nsi se excede se podria desmayar o podria morir\n")
            print(RESET)
        else:
            print("Tu nivel de energia actual  es: ", self.nivel_energia, "\n")
    def comersinRestricciones(self):
        print(f"{self.nombre} esta comiendo sin restricciones", self.nivel_energia)
        self.nivel_energia +=75
        if self.nivel_energia == 249:
            print()
            print(RED)
            print(f"{self.nombre} tienes la energia en ({self.nivel_energia}) y has muerto por que has excedido el nivel de energia maximo (250)\n")
            print("GAME OVER")
            print(RESET)
            print()
            exit()
        elif self.nivel_energia > 249:
            print()
            print(RED)
            print(f"{self.nombre} tienes la energia en ({self.nivel_energia}) y has muerto por que has excedido el nivel de energia maximo (250)\n")
            print("GAME OVER")
            print(RESET)
            print()
            exit()
        elif self.nivel_energia >= 180:
            print()
            print(MAGENTA)
            print(f"{self.nombre} tienes una energia de" ,{self.nivel_energia}, "esta por encima de la energia normal el maximo es (250)\nsi se excede se podria desmayar o podria morir\n")
            print(RESET)
        else:
            print("Tu nivel de energia actual  es: ", self.nivel_energia, "\n")
    def correr(self):
        print(f"{self.nombre} esta corriendo")
        self.nivel_energia -=20
        if self.nivel_energia == 39:
            print()
            print(RED)
            print(f"{self.nombre} has muerto por que has disminuido el nivel de energia minimo (40)", self.nivel_energia, "\n")
            print("GAME OVER")
            print(RESET)
            print()
            exit()
        elif self.nivel_energia < 39:
            print()
            print(RED)
            print(f"{self.nombre} has muerto por que has disminuido el nivel de energia minimo (40)", self.nivel_energia,"\n")
            print("GAME OVER")
            print(RESET)
            print()
            exit()
        elif self.nivel_energia <= 60:
            print()
            print(MAGENTA)
            print(f"{self.nombre} tienes una energia de" ,{self.nivel_energia}, "esta por debajo de la energia normal el minimo es (40) si se disminuye se podria desmayar o podria morir\n")
            print(RESET)
        else:
            print("Tu nivel de energia actual  es: ", self.nivel_energia,"\n")
    def verTV(self):
        print(f"{self.nombre} esta viendo TV")
        self.nivel_energia -=5
        if self.nivel_energia == 39:
            print()
            print(RED)
            print(f"{self.nombre} has muerto por que has disminuido el nivel de energia minimo (40)", self.nivel_energia, "\n")
            print("GAME OVER")
            print(RESET)
            print()
            exit()
        elif self.nivel_energia < 39:
            print()
            print(RED)
            print(f"{self.nombre} has muerto por que has disminuido el nivel de energia minimo (40)", self.nivel_energia, "\n")
            print("GAME OVER")
            print(RESET)
            print()
            exit()
        elif self.nivel_energia <= 60:
            print()
            print(MAGENTA)
            print(f"{self.nombre} tienes una energia de" ,{self.nivel_energia}, "esta por debajo de la energia normal el minimo es (40) si se disminuye se podria desmayar o podria morir")
            print(RESET)
        else:
            print("Tu nivel de energia actual  es: ", self.nivel_energia, "\n")
    def caminando(self):
        print(f"{self.nombre} esta caminando")
        self.nivel_energia -=10
        if self.nivel_energia == 39:
            print()
            print(RED)
            print(f"{self.nombre} has muerto por que has disminuido el nivel de energia minimo (40)", self.nivel_energia)
            print("GAME OVER")
            print(RESET)
            print()
            exit()
        elif self.nivel_energia < 39:
            print()
            print(RED)
            print(f"{self.nombre} has muerto por que has disminuido el nivel de energia minimo (40)", self.nivel_energia)
            print("GAME OVER")
            print(RESET)
            print()
            exit()
        elif self.nivel_energia <= 60:
            print()
            print(MAGENTA)
            print(f"{self.nombre} tienes una energia de" ,{self.nivel_energia}, "esta por debajo de la energia normal el minimo es (40) si se disminuye se podria desmayar o podria morir")
            print(RESET)
        else:
            print("Tu nivel de energia actual  es: ", self.nivel_energia, "\n")
            print()

#Funcion
    def user(self):

# Mostrar las opciones al usuario
        print()
        print(GREEN)
        print("Seleccione una opción:")
        for i in range(len(options)):
            print(str(i+1) + ". " + options[i])


#Pedir al usuario que seleccione una opción
        print()
        seleccion = int(input("Ingrese el número de la opción seleccionada: "))
        print(RESET)

# Validar la selección del usuario
        print(RED)
        if seleccion < 1 or seleccion > len(options):
            print("Selección inválida.")
            print(RESET)
            self.user()

        else:
            print(GREEN)
            print("Ha seleccionado la opción:", options[seleccion-1])
            print(RESET)

#Validaciones
        if options[seleccion-1] == 'Comer Sano':
            Ejecutar.comerSano()                   
        elif options[seleccion-1] == 'Dormir':
            Ejecutar.dormir()     
        elif options[seleccion-1] == 'Comer Sin Restricciones':
            Ejecutar.comersinRestricciones()     
        elif options[seleccion-1] == 'Correr':
            Ejecutar.correr() 
        elif options[seleccion-1] == 'Ver Tv':
            Ejecutar.verTV()    
        elif options[seleccion-1] == 'Caminar':
            Ejecutar.caminando()    
                

# INICIO DE PROGRAMA
print()
print("Bienvenido a la App Nivel de Energia")
print()
print()
print(BLUE)
nombre = str(input ("Ingrese su Nombre: "))
fechaN = str(input ("Ingrese la Fecha de Nacimiento: "))
cedula = int(input ("Ingrese su Cedula: "))
print(RESET)
print()
Ejecutar = Persona ( nombre, fechaN, cedula)

#Funcion Repetir el Juego
def jugar():
        while True:
            Ejecutar.user()
            print(CYAN)
            repetir = input ("Escribe 'S' para volver a realizar otra actividad o 'N' para TERMINAR: ").lower()
            print(RESET)
            if repetir != "s":
                print()
                print(RED)
                print("GAME OVER")
                print(RESET)
                print()
                break
jugar()
