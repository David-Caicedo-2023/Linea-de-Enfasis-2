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
5. Toda persona inicia el APP afirmando en las opciones una accion a ejecutar.
6. Busque controlar que todos los datos sean correctos

"""
options = ["comer sano", "dormir", "comer sin restricciones", "correr", "ver tv", "caminar"]

class Persona:
    def __init__(self,nombre,fecha_nac,cedula):
        self.nombre = nombre
        self.fecha_nac = fecha_nac
        self.cedula = cedula
        self.nivel_energia = energia = 80

    def comerSano(self):
        print(f"{self.nombre} esta comiendo sano")
        self.nivel_energia +=30
        if self.nivel_energia >= 250:
            print(f"{self.nombre} estas muerto", self.nivel_energia)
        else:
            print("Tu nivel de energia ha subido  y tiene un valor actual de: ", self.nivel_energia)
    def dormir(self):
        print(f"{self.nombre} esta durmiendo", self.nivel_energia)
        self.nivel_energia +=100
        if self.nivel_energia >= 250:
            print(f"{self.nombre} estas muerto", self.nivel_energia)
        else:
            print("Tu nivel de energia ha subido  y tiene un valor actual de: ", self.nivel_energia)
    def comersinRestricciones(self):
        print(f"{self.nombre} esta comiendo sin restricciones", self.nivel_energia)
        self.nivel_energia +=75
        if self.nivel_energia >= 250:
            print(f"{self.nombre} estas muerto", self.nivel_energia)
        else:
            print("Tu nivel de energia ha subido  y tiene un valor actual de: ", self.nivel_energia)
    def correr(self):
        print(f"{self.nombre} esta corriendo")
        self.nivel_energia -=20
        if self.nivel_energia == 0:
            print(f"{self.nombre} estas muerto", self.nivel_energia)
        elif self.nivel_energia < 0:
            print(f"{self.nombre} estas muerto", self.nivel_energia)
        elif self.nivel_energia <= 40:
            print(f"{self.nombre} esta por debajo de la energia normal y se podria desmayar o podria morir", self.nivel_energia)
        else:
            print("Tu nivel de energia actual  es: ", self.nivel_energia)
    def verTV(self):
        print(f"{self.nombre} esta viendo TV")
        self.nivel_energia -=5
        if self.nivel_energia == 0:
            print(f"{self.nombre} estas muerto", self.nivel_energia)
        elif self.nivel_energia < 0:
            print(f"{self.nombre} estas muerto", self.nivel_energia)
        elif self.nivel_energia <= 40:
            print(f"{self.nombre} esta por debajo de la energia normal y se podria desmayar o podria morir", self.nivel_energia)
        else:
            print("Tu nivel de energia actual  es: ", self.nivel_energia)
    def caminando(self):
        print(f"{self.nombre} esta caminando")
        self.nivel_energia -=10
        if self.nivel_energia == 0:
            print(f"{self.nombre} estas muerto", self.nivel_energia)
        elif self.nivel_energia < 0:
            print(f"{self.nombre} estas muerto", self.nivel_energia)
        elif self.nivel_energia <= 40:
            print(f"{self.nombre} esta por debajo de la energia normal y se podria desmayar o podria morir", self.nivel_energia)
        else:
            print("Tu nivel de energia actual  es: ", self.nivel_energia)
            
print("Bienvenido a la App Nivel de Energia")
nombre = str(input ("Ingrese su Nombre: "))
fechaN = str(input ("Ingrese la Fecha de Nacimiento: "))
cedula = int(input ("Ingrese su Cedula: "))
Ejecutar = Persona ( nombre, fechaN, cedula)
def user():
    optionUser = input("Piensa y Escribe una de estas opciones: \n Comer Sano \n Dormir \n Comer sin Restricciones \n Correr \n Ver Tv \n Caminar \n").lower()
    if optionUser not in options:
        print ("Opcion No Valida \nIntenta De Nuevo \n")
        user()
    elif optionUser == "comer sano":
        Ejecutar.comerSano()
    elif optionUser == "dormir":
        Ejecutar.dormir()
    elif optionUser == "comer sin restricciones":
        Ejecutar.comersinRestricciones()
    elif optionUser == "correr":
        Ejecutar.correr()
    elif optionUser == "ver tv":
        Ejecutar.verTV()
    elif optionUser == "caminar":
        Ejecutar.caminando()

def jugar():
        while True:
            user()
            repetir = input ("Escribe 'S' para volver a realizar otra actividad o 'N' para TERMINAR: ").lower()
            if repetir != "s":
                print("GAME OVER")
                break
jugar()
