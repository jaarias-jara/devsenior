#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Ejercicio 1: Clase Libro
Este archivo contiene la implementación de una clase Libro con sus atributos y métodos.
"""

class Libro:
    """
    Clase que representa un libro con título, autor y número de páginas.
    """
    
    def __init__(self, titulo, autor, paginas):
        """
        Constructor de la clase Libro
        
        Args:
            titulo (str): Título del libro
            autor (str): Nombre del autor del libro
            paginas (int): Número de páginas del libro
        """
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
    
    def descripcion(self):
        """
        Imprime una descripción del libro incluyendo título, autor y número de páginas.
        """
        print(f"Libro: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Páginas: {self.paginas}")
        print(f"El libro '{self.titulo}' fue escrito por {self.autor} y tiene {self.paginas} páginas.")

# Crear una instancia de la clase Libro con datos de ejemplo
mi_libro = Libro("Python para Todos", "Juan Pérez", 250)

# Acceder a los atributos de la instancia
print("Información del libro:")
print(f"Título: {mi_libro.titulo}")
print(f"Autor: {mi_libro.autor}")
print(f"Número de páginas: {mi_libro.paginas}")

# Llamar al método descripcion()
print("\nDescripción completa del libro:")
mi_libro.descripcion() 