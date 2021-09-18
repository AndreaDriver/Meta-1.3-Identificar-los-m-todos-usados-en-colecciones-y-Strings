"""""
DESCRIPCION: Contar Mayusculas y minusculas
AUTOR: Vara Espinoza Andrea Lizeth
FECHA DE CREACION: 13/09/21
ULTIMA MODIFICACION: 17/09/21
"""""

texto = input("TEXTO: ")

def funcionMinMax(texto):
    may = 0
    min = 0
    for element in texto:
        if element.isupper():
            may=may+1;
        if element.islower():
            min = min +1
    print("Mayuscula {}, Minisculas: {}".format(may, min))

funcionMinMax(texto)