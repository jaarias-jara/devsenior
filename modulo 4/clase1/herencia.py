class animal: #clase padre
    def __init__(self, nombre, edad):#constructor de la clase padre     
        self.nombre = nombre #atributo de la clase padre
        self.edad = edad #atributo de la clase padre

    def hablar(self):#metodo de la clase padre
        print("El animal hace un sonido")

class perro(animal): #clase hija                
    def __init__(self, nombre, edad, raza):#constructor de la clase hija
        super().__init__(nombre, edad)#llamada al constructor de la clase padre
        self.raza = raza#atributo de la clase hija

    def hablar(self):#metodo de la clase hija
        print(f"{self.nombre} dice: Guau")

mi_perro = perro("Firulais", 3, "Labrador") #instancia de la clase hija 

print(mi_perro.nombre)#acceso a los atributos de la clase padre
print(mi_perro.edad)#acceso a los atributos de la clase padre
print(mi_perro.raza)#acceso a los atributos de la clase hija
mi_perro.hablar()#acceso al metodo de la clase hija
