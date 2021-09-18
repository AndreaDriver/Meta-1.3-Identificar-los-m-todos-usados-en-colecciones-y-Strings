"""""
DESCRIPCION: Temperaturas de ciudades. A-Temperatura media B-Temperatura menor x c/ciudad C-La temperatura menor
AUTOR: Vara Espinoza Andrea Lizeth
FECHA DE CREACION: 13/09/21
ULTIMA MODIFICACION: 17/09/21
"""""

dic = {'Londres': [3.4, 6.3, 10.5], 'Oslo': [-3.8, -5.0, 4.2], 'Rennes': [2.5, 3.1, 12.3]}

#A
def mediaTemp(dic):
    media = 0
    dicMedia = {}
    for elemet in dic:
        lst = dic[elemet]
        cantidad = len(lst)
        i=0
        sum = 0
        num = 0
        while i < cantidad:
            num = lst[i]
            sum = sum + num
            i+=1
        n = round(sum / cantidad, 2)
        dicMedia[elemet] = n
    return dicMedia

#B
def minimasTemp(dic):
    dicMin = {}
    lstMin = []

    for elemet in dic:
        lst = dic[elemet]
        lst.sort() #lista en forma descendente
        num = lst[0]
        dicMin[elemet] = num
    return dicMin


dicMin2 = {}
nMen = 0
#C
def minTemp(dic):
    dicMenor = {}
    global dicMin2
    for elemet in dic:

        lst = dic[elemet]
        lst.sort()  # lista en forma descendente
        num = lst[0]
        dicMin2[elemet] = num # diccionario de menor

    #list(dicMin2.items())
    lst2 = []
    listaResultado = []


    for elemet in dicMin2:
        global nMen
        lst1 = dicMin2[elemet]
        lst2.append(lst1) #lista solo numeros
    lst2.sort()
    nMen = lst2[0] #numero menor

    listaResultado.append(list(dicMin2.keys())[list(dicMin2.values()).index(nMen)])
    listaResultado.append(nMen)
    return listaResultado


print('La media de temperaturas por ciudad es: ', mediaTemp(dic))
print('Las menores temperaturas de cada ciudad son: ', minimasTemp(dic))
print('La ciudad con menor temperatura: ', minTemp(dic))