import datetime

def validar_fecha(fecha_str):
    try:
        datetime.datetime.strptime(fecha_str, "%d/%m/%Y")
        return True
    except ValueError:
        return False

def agregar_experimento(experimentos):
    nombre = input("Nombre del experimento: ")
    fecha = input("Fecha de realización (DD/MM/AAAA): ")
    while not validar_fecha(fecha):
        print("Fecha inválida. Intente nuevamente.")
        fecha = input("Fecha de realización (DD/MM/AAAA): ")
    tipo = input("Tipo de experimento (Química, Biología, Física): ")
    resultados = list(map(float, input("Resultados (separados por espacios): ").split()))
    experimento = {
        "nombre": nombre,
        "fecha": fecha,
        "tipo": tipo,
        "resultados": resultados
    }
    experimentos.append(experimento)
    print("Experimento agregado con éxito.")

def ver_experimentos(experimentos):
    for i, exp in enumerate(experimentos):
        print(f"{i+1}. Nombre: {exp['nombre']}, Fecha: {exp['fecha']}, Tipo: {exp['tipo']}, Resultados: {exp['resultados']}")

def calcular_promedio(resultados):
    return sum(resultados) / len(resultados)

def calcular_maximo(resultados):
    return max(resultados)

def calcular_minimo(resultados):
    return min(resultados)

def analizar_resultados(experimentos):
    ver_experimentos(experimentos)
    seleccion = int(input("Seleccione el número del experimento a analizar: ")) - 1
    if 0 <= seleccion < len(experimentos):
        exp = experimentos[seleccion]
        resultados = exp["resultados"]
        print(f"Promedio: {calcular_promedio(resultados)}")
        print(f"Máximo: {calcular_maximo(resultados)}")
        print(f"Mínimo: {calcular_minimo(resultados)}")
    else:
        print("Selección inválida.")

def generar_informe(experimentos):
    with open("informe.txt", "w") as file:
        file.write("Informe de Experimentos\n")
        file.write("======================\n")
        for exp in experimentos:
            file.write(f"Nombre: {exp['nombre']}\n")
            file.write(f"Fecha: {exp['fecha']}\n")
            file.write(f"Tipo: {exp['tipo']}\n")
            file.write(f"Resultados: {exp['resultados']}\n")
            file.write(f"Promedio: {calcular_promedio(exp['resultados'])}\n")
            file.write(f"Máximo: {calcular_maximo(exp['resultados'])}\n")
            file.write(f"Mínimo: {calcular_minimo(exp['resultados'])}\n")
            file.write("\n")
    print("Informe generado con éxito.")

def menu():
    experimentos = []
    while True:
        print("\nMenú de Opciones")
        print("1. Agregar Experimento")
        print("2. Ver Experimentos")
        print("3. Analizar Resultados")
        print("4. Generar Informe")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            agregar_experimento(experimentos)
        elif opcion == "2":
            ver_experimentos(experimentos)
        elif opcion == "3":
            analizar_resultados(experimentos)
        elif opcion == "4":
            generar_informe(experimentos)
        elif opcion == "5":
            break
        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    menu()