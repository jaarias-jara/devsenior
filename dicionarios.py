carro = {
         "marca":"mazda",
         "modelo":"626",
         "annio":"1985",
         "colores":["rojo","azul","amarillo"]
         }#no permite elementos repetido
#print(carro["modelo"])
print(carro)
#print(len(carro))# imprime la lonjitud del carro
#print(type(carro))#para ver el tipo de clase
print(carro.keys())# muestra las llaves
print(carro.values())#muestra el valor de las llaves
carro["marca"]= "renault"#remuee la marca mazda
print(carro)
print(carro.items())