import os
import time  # Para añadir una pequeña pausa antes de limpiar la pantalla

class Coche:# clase coche   
    def __init__(self, marca, modelo, ano):#constructor
        # Atributos privados
        self.__marca = marca
        self.__modelo = modelo
        self.__ano = ano
    
    # Métodos para obtener los valores de los atributos privados
    def get_marca(self):#metodo obtener marca
        return self.__marca
    
    def get_modelo(self):#metodo obtener modelo
        return self.__modelo #retorna el modelo
    
    def get_ano(self):#metodo obtener ano
        return self.__ano #retorna el ano
    
    # Método para saludar
    def saludar(self):#metodo saludar
        print(f"Hola, soy un {self.__marca} {self.__modelo} del año {self.__ano}.")#imprime el mensaje  
    
    # Desafío adicional: método para actualizar el año
    def set_ano(self, nuevo_ano):#metodo actualizar ano         
        if nuevo_ano > self.__ano:#si el nuevo ano es mayor al ano actual
            self.__ano = nuevo_ano#actualiza el ano
            return True#retorna true
        else:
            return False#retorna false  


# Ejemplo de uso
if __name__ == "__main__": #si el archivo se ejecuta como programa principal    
    # Crear un objeto de la clase Coche
    mi_coche = Coche("Toyota", "Corolla", 2020) #instancia de la clase coche
    
    # Llamar al método saludar
    mi_coche.saludar() #llama al metodo saludar
    
    # Probar los métodos get
    print(f"Marca: {mi_coche.get_marca()}") #imprime la marca
    print(f"Modelo: {mi_coche.get_modelo()}") #imprime el modelo
    print(f"Año: {mi_coche.get_ano()}") #imprime el ano
    
    # Probar el método set_ano
    if mi_coche.set_ano(2023):#si el año es mayor al año actual
        print(f"Año actualizado a: {mi_coche.get_ano()}")#imprime el nuevo ano
    else:
        print("No se pudo actualizar el año")#imprime el mensaje
    
    # Intentar actualizar a un año menor
    if mi_coche.set_ano(2021):#si el año es menor al año actual
        print(f"Año actualizado a: {mi_coche.get_ano()}")#imprime el nuevo ano
    else:
        print("No se pudo actualizar el año (debe ser mayor al año actual)") #imprime el mensaje
    
    # Pausa para que el usuario pueda ver los resultados antes de limpiar la pantalla
    print("\nEl programa terminará y la pantalla se limpiará en 3 segundos...")
    time.sleep(13)
    
    # Limpiar la pantalla según el sistema operativo
    if os.name == "nt":  # Para Windows
        os.system("cls")
    else:  # Para Unix (Linux, macOS)
        os.system("clear")