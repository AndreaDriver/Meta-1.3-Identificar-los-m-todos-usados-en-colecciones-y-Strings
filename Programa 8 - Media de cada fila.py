"""""
DESCRIPCION: Media de cada lista, de una lista de listas
AUTOR: Vara Espinoza Andrea Lizeth
FECHA DE CREACION: 13/09/21
ULTIMA MODIFICACION: 17/09/21
"""""

nff = 0

def ingreso_matriz():
    nf = int(input("# de filas: "))
    nc = int(input("# de columnas: "))
    global nff
    global ncc
    ncc = nc
    nff = nf
    f=0

    lista = []
    listaM = []
    while f < nf:
        c = 0
        while c < nc:
            num = int(input("#: "))
            lista.append(num)
            c+=1
        listaC = lista.copy()
        print("Lista: ", listaC)
        listaM.append(listaC)
        lista.clear()
        f+=1
    return listaM

def media_filas(lst):
    global nff
    global ncc
    global  nc
    sum = 0
    suma=[]
    f = 0
    while f < nff:
        c = 0
        sum=0
        n = 0
        while c < ncc:
            num = lst[f][c]
            sum = sum + num
            c+=1
        n = sum/ncc
        suma.append(round(n,2))
        f +=1
    return suma

lst = []
lst = ingreso_matriz()
print("Resultado: ",media_filas(lst))