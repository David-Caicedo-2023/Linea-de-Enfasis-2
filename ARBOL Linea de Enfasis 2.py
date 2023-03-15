BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[39m' '\033[30m'

class Node:
    def __init__(self, value):
        self.value = value #raiz, el valor del nodo
        self.left = None
        self.right = None

def preorden(node):
    if node is None:
        return
    print(node.value, end=" ")
    preorden(node.left)
    preorden(node.right)

def postorden(node):
    if node is None:
        return
    postorden(node.left)
    postorden(node.right)
    print(node.value, end =" ")

def inorden(node):
    if node is None:
        return
    inorden(node.left)
    print(node.value, end =" ")
    inorden(node.right)
    

#Crear Arbol
root = Node('A')
root.left =Node('B')
root.right = Node('C')
root.left.left= Node('D')
root.left.right= Node('E')
root.right.left= Node ('F')
root.right.right= Node ('G')

print(RED)
print("Recorrido Preorden")
preorden(root)
print(RESET)

print(GREEN)
print("\n Recorrido Preorden")
postorden(root)
print(RESET)

print(BLUE)
print("\n Recorrido Inorden")
inorden(root)
print(RESET)