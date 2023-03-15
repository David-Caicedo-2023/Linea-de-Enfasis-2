def solicitarNombre():
    nombre = input("Hola, ingresa tu nombre: ")
    imprimir(nombre)

def solicitarEdad():
    edad = int(input("Ingrese la edad: "))
    imprimir(edad)

def imprimir(a):
    print("El resultado es: ", a)

solicitarNombre()