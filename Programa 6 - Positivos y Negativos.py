"""""
DESCRIPCION: De una lista obtener numeros positivos y negativos
AUTOR: Vara Espinoza Andrea Lizeth
FECHA DE CREACION: 13/09/21
ULTIMA MODIFICACION: 17/09/21
"""""
cadena = (input("Ingresa cadena, Ejemplo: 69,-37,0,-27,-59,83,1,45: "))
lst0 = (cadena.split(','))
lst= [int(x) for x in lst0]
#print(lst)


def PositNegat(lst):
    listaPositiva = [element for element in lst if element >=0]
    listaNegativa = [element for element in lst if element < 0]
    return "Lista negativa: {}, Lista Negativa{}".format(listaNegativa, listaPositiva)

print(PositNegat(lst))