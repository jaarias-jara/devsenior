"""
frutas = ["fresas","papaya","manzana", "pera",5,True]
print(frutas[5])
# ordenadas, mutables, permiten duplicados
valoresdeverdad = [True, True, False, True]
edades = [53,58,93,8]
evaluaciones = [3.5,9.3,2.8]
ensayis = ["carlos", [1,6,8],52,True]
print(len(frutas))
print(type(frutas))

nombre = "carlos"
mazda =[626, 323, "cx2", nombre]
carros = mazda
#metodo constructor
frutas = ["manzana", "papaya", "pera", "piña", "guanabana"]

print(frutas[1:3])

frutas = ["manzana", "papaya", "pera", "piña", "guanabana"]
print("manzana" in frutas)

frutas = ["manzana", "papaya", "pera", "piña", "guanabana"]
frutas.append("naranja")
print(frutas)
#frutas.clear()
frutas2=frutas.copy()
print(frutas2)
frutas2.append("mandarina")
print(frutas2)
print(frutas)

frutas = ["manzana", "papaya", "pera", "piña", "guanabana"]
frutasmalucas = ["chontaduro", "marañom"]
print(frutas.count("papaya")) #cuenta la cantidad de frutas selecionadas
frutas.extend(frutasmalucas)
print(frutas)
print(frutas.index("piña"))#muestra la posicion de la fruta
frutas.insert(1,"guayaba") #inserta la fruta en la posicion que yo quiera
print(frutas)
frutas = ["manzana", "papaya", "pera", "piña", "guanabana"]
frutas[1]="toronja"#reemplza la papaya en la posicion 1
print(frutas)

frutas = ["manzana", "papaya", "pera", "piña", "guanabana"]
frutas.pop()#borra la ultima tambien borra la posicion que le diga
print(frutas)

frutas = ["manzana", "papaya", "pera", "piña", "guanabana"]
frutas.remove("pera") #remueve el elemento que yo le diga
print(frutas)
frutas.reverse()# las muestra al reves
print(frutas)
frutas.sort()
print(frutas)
"""