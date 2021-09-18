"""""
DESCRIPCION: Numeros sin repetir
AUTOR: Vara Espinoza Andrea Lizeth
FECHA DE CREACION: 13/09/21
ULTIMA MODIFICACION: 17/09/21
"""""
lista = list()
ee = list()

def uniqueNumbers():
    i = 1
    global lista
    global ee
    while i <=5:
        e = int(input("DAME UN NUMERO "))
        ee.append(e)
        bb = ee.count(e)

        if bb == 1:
            i = i + 1
            lista.append(e)
    return lista

print(uniqueNumbers())