# Definir la clase persona con encapsulamiento      
class Persona:
    # Método constructor
    def __init__(self, nombre, edad):
        # Atributos con encapsulamiento
        self.__nombre = nombre  # Privado
        self.__edad = edad      # Privado
    
    # Métodos getter y setter (encapsulamiento)
    def get_nombre(self):
        return self.__nombre
        
    def set_nombre(self, nombre):
        self.__nombre = nombre
        
    def get_edad(self):
        return self.__edad
        
    def set_edad(self, edad):
        if edad > 0:  # Validación
            self.__edad = edad
    
    # Método para saludar
    def saludar(self):
        print(f"¡Hola! Mi nombre es {self.__nombre} y tengo {self.__edad} años.")

# Clase que hereda de Persona
class Estudiante(Persona):
    def __init__(self, nombre, edad, carrera):
        # Llamar al constructor de la clase padre
        super().__init__(nombre, edad)
        self.carrera = carrera
        
    # Sobrescribir el método saludar
    def saludar(self):
        super().saludar()
        print(f"Estudio {self.carrera}.")

# Crear objetos
persona1 = Persona("Juan", 25)
estudiante1 = Estudiante("María", 20, "Informática")

# Usar los métodos
persona1.saludar()
estudiante1.saludar()