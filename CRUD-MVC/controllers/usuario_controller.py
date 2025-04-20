from models.usuario import Usuario # importar la clase Usuario
from utils.logger import Log_error, Log_info # importar funciones de log

class GestUsarios: # clase para gestionar usuarios
    """Clase para gestionar usuarios"""
    def __init__(self): #metodo el constructor
        self.usuarios = {} #diccionario para almacenar los usuarios

    def crear_usuario(self, usuario: Usuario):# metodo para crear un usuario
        try #para manejar errores excepciones 
            if usuario.id in self.usuarios:# verificar si el usuario ya existe
                raise ValueError("El usuario ya existe.")# lanzar una excepcion
            self.usuarios[usuario.id] = usuario #almacenar el usuario en el diccionario 
            Log_info(f"Usuario con ID: {usuario.id}")  # registrar el usuario creado
            return True #retornar verdadero si el usuario fue creado
        except Exception as e: # manejar la excepcion
            Log_error(f"Error al crear usuario: {e}") # registrar el error
            return False #retornar falso si hubo un error al crear el usuario
        
    def obtener_usuario(self): # metodo para obtener un usuario
        return list(self.usuarios.values()) #retornar la lista de usuarios
    
    def actualizar_usuario(self, id_usuario:int, nombre = None, correo = None): # metodo para actualizar un usuario 
        try:
            usuario = self.usuarios.get(id_usuario) # obtener el usuario por su id
            if not usuario: # verificar si el usuario existe
                raise ValueError("El usuario no existe.") # lanzar una excepcion        
            if nombre:
                usuario.nombre = nombre
            if correo:
                usuario.correo = correo
            
            Log_info(f"Usuario con ID: {id_usuario} actualizado.") # registrar el usuario actualizado   
        except Exception as e: # manejar la excepcion
            Log_error(f"Error al actualizar usuario: {e}") # registrar el error
            return False #retornar falso si hubo un error al actualizar el usuario

    def eliminar_usuario(self, id_usuario:int): # metodo para eliminar un usuario
        try: # obtener el usuario por su id 
            if id_usuario not in self.usuarios: # verificar si el usuario existe
                raise ValueError("El usuario no existe.") # lanzar una excepcion
            del self.usuarios[id_usuario] # eliminar el usuario del diccionario
            Log_info(f"Usuario con ID: {id_usuario} eliminado.") # registrar el usuario eliminado
            return True #retornar verdadero si el usuario fue eliminado
        except Exception as e: # manejar la excepcion
            Log_error(f"Error al eliminar usuario: {e}") # registrar el error
            return False #retornar falso si hubo un error al eliminar el usuario