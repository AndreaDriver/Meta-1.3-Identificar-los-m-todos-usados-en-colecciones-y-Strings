"""""
DESCRIPCION: Mover los elementos de una lista hacia la derecha
AUTOR: Vara Espinoza Andrea Lizeth
FECHA DE CREACION: 13/09/21
ULTIMA MODIFICACION: 17/09/21
"""""

cadena = (input("Ingresa lista (x,y,z): "))
lst0 = (cadena.split(','))
lst= [int(x) for x in lst0]
#cadena.reverse()
#print(cadena)

#CADENA DE DERECHA A IZQUIERDA
def mueve_derecha(lst):
    lst1 = lst.copy()
    lst1.reverse()
    print(lst1)


#ULTIMO ELEMENTO A LA DERECHA
def ultimo_derecha(lst):
    i = lst[-1]
    lst.pop(-1)
    lst.insert(0, i)
    print(lst)


mueve_derecha(lst)
ultimo_derecha(lst)