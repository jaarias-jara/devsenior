def mostrar_menu():
    print("----- Menu opciones -----")
    print("1. Crear usuario")
    print("2. Leer ususuario")
    print("3. Actualizar usuario")
    print("4. Eliminar usuario")
   ## print("5. Listar Consolas")
    print("5. Salir")
    
    def pedir_datos_usuario():
        id_= input("Ingrese el ID del usuario: ")
        nombre = input("Ingrese el nombre del usuario: ")
        email = input("Ingrese el email del usuario: ")
        return id_, nombre, email
    
    def mostrar_usuario(usuario):
        if not usuario:
            print("No se encontró el usuario.")
        else:
            for u in usuario:
                print(u.mostrar_info())
                
    def mensaje(mensaje):
        print(mensaje)
        