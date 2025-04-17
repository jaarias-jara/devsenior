"""
try:
    with open("datos.txt", "r") as archivo: #archivo r tipo lectura
        contenido = archivo.read()
        numero= int(contenido.strip())
        resultado = 100/ numero
        print(f"el resultado es:{resultado}")
except Exception as e:
    print(f"se genero un ERROR:{e}")
    
def division_segura_dos():
    try:
        numerador = int(input("ingrese el numerdador: "))
        denominador = int(input("ingrese el denominador "))
        resultado = numerador / denominador
        print(f"el resultado de la division es: {resultado10}")
    except (ZeroDivisionError, ValueError) as e: #manejo de multiples excepciones
        print("Error : {e}")

division_segura_dos()
    
    numero = int(input("ingrese el numero : "))
    resultado = 10/numero 
    print(f"el resultado es : {resultado} ")
except ValueError as e:
    print(f"error: entrada invalida. {e}")
except ZeroDivisionError as e:
    print(f"Error: no se puede realizar la division entre cero: ")
else:
    print(f"el resultado es: {resultado}")
finally:
    print("ejercicio finalizado")

def procesar_pedido(codigo_producto, cantidad):
    try:
        #simular una validacion de datos
        if not codigo_producto.isalnum():
            #raise error: gestiona de forma manual y en tiempo de ejecucion un error
            raise ValueError("el codigo del producto debe ser alfa numerico")
        if cantidad <= 0:
            raise ValueError("la cantidad debe ser superior a cero")
        #simular el calculo del total.
        precio_unitario = 100 #ejemplo de precio por uniad
        total = precio_unitario * cantidad
        
    except ValueError as e:
        print(f"error al procesar un pedido: {e}")
    else:
        print(f"pedido procesado exitosamente. el total a pagar es: ${total:.2f}")
    finally:
        print("operacion finalizada, registro actualizado")

#metodo pricipal

if __name__ == "__main__":
    procesar_pedido("ABC123",2)
    procesar_pedido("####",12)
    procesar_pedido("GHJ8547", -10)
  """
class ErrorDePago(Exception):
    pass

class PasareLaDepago:
    @staticmethod
    def procesar_pago(numero_tarjeta, monto):
        if not numero_tarjeta.startswith("4"):
            raise ErrorDePago("el numero de la tarjeta no es valido. debe iniciar en 4")
        if monto <= 0:
            raise ErrorDePago("el monto de la compra debe ser superior a cero")
        if len(numero_tarjeta) != 16:
            raise ErrorDePago("el numero de tarjeta debe tener 16 digitos")
        
        return f"el pago de ${monto} fue procesado con exito."
def proceso_pago_cliente(nombre_cliente, numero_tarjeta, monto):
    try:
        print(f"iniciando el proceso de pago de {nombre_cliente}...")
        resultado = PasareLaDepago.procesar_pago()
        