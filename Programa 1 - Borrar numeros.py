"""""
DESCRIPCION: Borrar Números en string
AUTOR: Vara Espinoza Andrea Lizeth
FECHA DE CREACION: 12/09/21
ULTIMA MODIFICACION: 17/09/21
"""""
ingresoStrin = input("Escribe algo: ")
ingresoStrin2 = ""

def metodo(ingresoString):
    global ingresoStrin2
    for element in ingresoStrin:

        if element.isalpha() or element == " ":
            ingresoStrin2 = ingresoStrin2 + element
    return ingresoStrin2

print(metodo(ingresoStrin))