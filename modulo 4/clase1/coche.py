class Coche:
    # Constructor de la clase
    def __init__(self, marca, modelo, año):
        # Inicialización de atributos
        self.marca = marca
        self.modelo = modelo
        self.año = año
    
    # Método para mostrar información del coche
    def informacion(self):
        print(f"Información del coche:")
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Año: {self.año}")

# Crear una instancia de la clase Coche
mi_coche = Coche("Toyota", "Corolla", 2020)

# Acceder a los atributos
print("Accediendo a los atributos:")
print(f"Marca: {mi_coche.marca}")
print(f"Modelo: {mi_coche.modelo}")
print(f"Año: {mi_coche.año}")

# Llamar al método informacion()
print("\nLlamando al método informacion():")
mi_coche.informacion() 