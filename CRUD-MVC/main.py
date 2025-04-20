from controller.usuario_controller import GestUsarios # type: ignore # importar la clase GestUsarios
from models.usuario import Usuario
from views.consola_view import mostrar_menu, pedir_datos_usuario, mostrar_usuario, mensaje

def main():
    gestor_usuarios = gestor_usuarios()
    while True:
        mostrar_menu() # Mostrar el menú de opciones
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            try:
                id_, nombre, email = pedir_datos_usuario() # Pedir datos del usuario
                usuario = Usuario(id_, nombre, email) # Crear un nuevo objeto Usuario
                if gestor.crear_usuario(usuario):
                    mensaje("Usuario creado exitosamente.") ## Mensaje de éxito
                else:
                    mensaje("Error al crear el usuario.")
            except Exception as e:
                mensaje(f"Error en los datos ingresados: {e}")
        
        elif opcion == '2':
                usuario = obtener_usuarios()
                mostrar_usuario(usuario)  # Mostrar el usuario
            
        elif opcion == '3':
            try:
                id_ = input("Ingrese el ID del usuario a actualizar: ") # Pedir ID del usuario a actualizar
                nombre = input("Ingrese el nuevo nombre del usuario: ") # Pedir nuevo nombre   
                email = input("Ingrese el nuevo email del usuario: ") # Pedir nuevo email
                if gestor_usuarios.actualizar_usuario(id_, nombre, email):# Actualizar el usuario
                    mensaje("Usuario actualizado exitosamente.")## Mensaje de éxito
                else:
                    mensaje("Error al actualizar el usuario.")# Mensaje de error
            except Exception as e:# Manejo de excepciones
                mensaje(f"Error en los datos ingresados: {e}") # Mensaje de error    
                
        elif opcion == '4':
            try:
                id_ = input("Ingrese el ID del usuario a eliminar: ") # Pedir ID del usuario a eliminar
                if gestor_usuarios.eliminar_usuario(id_):# Eliminar el usuario
                    mensaje("Usuario eliminado exitosamente.")# Mensaje de éxito
                else:
                    mensaje("Error al eliminar el usuario.")# Mensaje de error          
            except Exception as e:# Manejo de excepciones
                mensaje(f"Error en los datos ingresados: {e}")
                
        elif opcion == '5':# Salir del programa
            mensaje("Saliendo...") # Mensaje de salida
            break # Salir del bucle
        else:
            mensaje("Opción inválida. Intente nuevamente.") # Mensaje de opción inválida

if __name__ == "__main__": # Verificar si el script se está ejecutando directamente
