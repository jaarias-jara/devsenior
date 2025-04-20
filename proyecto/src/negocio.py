from abc import ABC, abstractmethod
from dataclasses import dataclass   

@dataclass
class vendedor(ABC):
    """_summary_

    Args:
        ABC (_type_): _description_
    """
    nombre: str
    ventas: float
    
    @abstractmethod
    def calcular_comision(self)-> float:
        """bloque de codigo"""
        pass

@dataclass
class VendedorBase(vendedor):
    """implementacion concreta de un vendedor con una comision por venta del 10%"""
    def calcular_comision(self) -> float:
        returnself.ventas * 0.10

@dataclass
class VendedorPremium(vendedor):
    """
    implementacion concreta de un vendedor con una comision por ventas de 15%
    """
    
    def calcular_comision(self):
        return self.ventas * 0.15
    