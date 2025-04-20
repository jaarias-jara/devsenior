import pdb
from abc import ABC, abstractmethod
from dataclasses import dataclass

#clase abstrata empleado
@dataclass
class Empleado(ABC):
    nombre: str
    salario_base: float
    
    @abstractmethod
    def calcular_salario(self):
        pass
    
@dataclass
class Manager(Empleado):
    
    def calcular_salario(self):
        return self.calcular_salario + 5000


@dataclass
class Developer(Empleado):
    
    def calcular_salario(self):
        return self.calcular_salario + 2000

def calcular_total_salario(empleado: Empleado) -> float:
    
    #pdb.set_trace()
    return empleado.calcular_salario()

if __name__=="__main__":
    Manager = Manager("carlos", 5000)
    Developer = Developer("pedro", 2000)
    
    print(calcular_total_salario(Manager))
    print(calcular_total_salario(Developer))