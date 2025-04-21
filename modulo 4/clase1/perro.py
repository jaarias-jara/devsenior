class Perro: #clase perro
    def __init__(self, nombre): #constructor
        self._nombre = nombre
        
    def obtener_nombre(self): #metodo obtener nombre
        return self._nombre
    
    def cambiar_nombre(self, nuevo_nombre): #metodo cambiar nombre
        self._nombre = nuevo_nombre

# Solicitar datos por teclado
nombre_inicial = input("Ingresa el nombre inicial del perro: ")
mi_perro = Perro(nombre_inicial) #instancia de la clase perro con nombre ingresado
print(f"Nombre actual del perro: {mi_perro.obtener_nombre()}") #imprime el nombre del perro

nuevo_nombre = input("Ingresa el nuevo nombre del perro: ")
mi_perro.cambiar_nombre(nuevo_nombre) #cambia el nombre del perro con el nuevo valor ingresado
print(f"Nuevo nombre del perro: {mi_perro.obtener_nombre()}") #imprime el nuevo nombre del perro



