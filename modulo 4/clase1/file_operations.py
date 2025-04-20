#!/usr/bin/env python
# Demostración de Operaciones con Archivos - Mostrando la función open() con diferentes modos
import argparse

def leer_archivo():
    """
    Lee e imprime el contenido de un archivo usando el modo 'r' (solo lectura)
    """
    try:
        with open("jaime.txt", 'r') as archivo:
            contenido = archivo.read()
            print(f"--- Contenido de jaime.txt (modo lectura) ---")
            print(contenido)
    except FileNotFoundError:
        print(f"Error: Archivo 'jaime.txt' no encontrado")
    except Exception as e:
        print(f"Error al leer el archivo: {e}")

def escribir_archivo(texto):
    """
    Escribe texto en un archivo usando el modo 'w' (modo escritura - crea un archivo nuevo o sobrescribe el existente)
    """
    try:
        with open("jaime.txt", 'w') as archivo:
            archivo.write(texto)
        print(f"Se escribió correctamente en jaime.txt")
    except Exception as e:
        print(f"Error al escribir en el archivo: {e}")

def agregar_archivo(texto):
    """
    Agrega texto a un archivo usando el modo 'a' (modo agregar - crea el archivo si no existe)
    """
    try:
        with open("jaime.txt", 'a') as archivo:
            archivo.write(texto)
        print(f"Se agregó correctamente a jaime.txt")
    except Exception as e:
        print(f"Error al agregar al archivo: {e}")

def leer_escribir_archivo(nuevo_texto=None):
    """
    Abre un archivo en modo 'r+' (modo lectura y escritura - el archivo debe existir)
    Lee el contenido y opcionalmente escribe nuevo texto en la posición actual
    """
    try:
        with open("jaime.txt", 'r+') as archivo:
            # Leer contenido actual
            contenido = archivo.read()
            print(f"--- Contenido actual de jaime.txt (modo lectura/escritura) ---")
            print(contenido)
            
            # Escribir nuevo contenido si se proporciona
            if nuevo_texto:
                archivo.seek(0)  # Mover al principio del archivo
                archivo.write(nuevo_texto)
                archivo.truncate()  # Eliminar cualquier contenido restante
                print(f"Se actualizó correctamente jaime.txt")
    except FileNotFoundError:
        print(f"Error: Archivo 'jaime.txt' no encontrado. El modo 'r+' requiere que el archivo exista.")
    except Exception as e:
        print(f"Error al acceder al archivo: {e}")

def ejecutar_operacion(modo):
    """Ejecuta la operación de archivo según el modo especificado"""
    if modo == 'r':
        leer_archivo()
    elif modo == 'w':
        texto = input("Ingrese el texto a escribir: ")
        escribir_archivo(texto)
    elif modo == 'a':
        texto = input("Ingrese el texto a agregar: ")
        agregar_archivo(texto)
    elif modo == 'r+':
        respuesta = input("¿Desea modificar el archivo? (s/n): ").lower()
        if respuesta == 's':
            texto = input("Ingrese el nuevo texto: ")
            leer_escribir_archivo(texto)
        else:
            leer_escribir_archivo()
    else:
        print(f"Modo de operación no válido: {modo}")
        print("Modos válidos: r (lectura), w (escritura), a (agregar), r+ (lectura/escritura)")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Operaciones de archivo con diferentes modos')
    parser.add_argument('modo', choices=['r', 'w', 'a', 'r+'], 
                        help='Modo de operación: r (lectura), w (escritura), a (agregar), r+ (lectura/escritura)')
    
    args = parser.parse_args()
    
    print("Demostración de Operaciones con Archivos")
    print("=======================================")
    print(f"Modo seleccionado: {args.modo}")
    ejecutar_operacion(args.modo)