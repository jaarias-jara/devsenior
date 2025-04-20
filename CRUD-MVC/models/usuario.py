from abc import ABC, abstractmethod
from dataclasses import dataclass

class UsuarioBase(ABC):
    
    @abstractmethod
    def mostrar_info(self):
        pass
    @dataclass
    class Usuario(UsuarioBase):
        __id: int
        __nombre: str
        __correo: str
        
        @property
        def id(self):       
            return self.__id
        
        @id.setter
        def id(self,nuevo_id):
            if isinstance(nuevo_id, int) and nuevo_id > 0:
                self.__id = nuevo_id
            else:
                raise ValueError("El id debe ser un número entero positivo.")
        
        def mostrar_info(self):
            return f"usuario: {self.nombre},email: {self.correo}"