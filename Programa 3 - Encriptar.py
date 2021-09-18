"""""
DESCRIPCION: Encriptar mensaje dependiendo de una clave
AUTOR: Vara Espinoza Andrea Lizeth
FECHA DE CREACION: 13/09/21
ULTIMA MODIFICACION: 17/09/21
"""""

s = input("Mensaje ") #cafe
clave = input("Clave ") #ixmrklstnuzbowfaqejdcpvhyg
encriptado = " "
def encripta(s, clave):
    i=0
    minClave = ""
    minMensaje = ""
    minClave = clave.lower()
    minMensaje = s.lower()

    s.lower()
    for element in minClave:
        i+=1
    if i == 26:

        global encriptado
        ABC = "abcdefghijklmnopqrstuvwxyz"

        for element in minMensaje:
            if element.isalpha():
                i = ABC.find(element)
                encriptado = encriptado + minClave[i]
            else:
                i = element
                encriptado = encriptado + i
        print(encriptado)
    else:
        print("ERROR EN CLAVE")

encripta(s, clave)