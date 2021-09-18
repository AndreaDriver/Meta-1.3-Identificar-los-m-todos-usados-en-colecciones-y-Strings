"""""
DESCRIPCION: Dada una lista de números naturales, devuelve un diccionario con el número de veces que aparece
cada número en la lista dada.
AUTOR: Vara Espinoza Andrea Lizeth
FECHA DE CREACION: 13/09/21
ULTIMA MODIFICACION: 17/09/21
"""""

def ingreso_lista():
    cadena = (input("Ingresa cadena (con ,): ")) #1, 3, 2, 4, 2, 2, 3, 2, 4, 1, 2, 1, 2, 3, 1, 3, 1
    lst0 = (cadena.split(','))
    lst = [int(x) for x in lst0]
    return lst

def frecuencias(lst):
    diccionario = {}
    s2 = set(lst) #no elementos repetidos
    for element in s2:
       n= lst.count(element)
       diccionario[element]=n
    print(diccionario)

frecuencias(ingreso_lista())