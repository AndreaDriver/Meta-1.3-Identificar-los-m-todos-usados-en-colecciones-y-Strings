"""""
DESCRIPCION: Desencriptar mensaje por clave
AUTOR: Vara Espinoza Andrea Lizeth
FECHA DE CREACION: 13/09/21
ULTIMA MODIFICACION: 17/09/21
"""""
s = input("Mensaje ") #milk
clave = input("Clave ") #ixmrklstnuzbowfaqejdcpvhyg
desencriptado = " " #cafe

def  desencripta(s, clave):
    i = 0
    for element in clave:
        i += 1
    if i == 26:

        global desencriptado
        ABC = "abcdefghijklmnopqrstuvwxyz"

        for element in s:
            if element.isalpha():
                i = clave.find(element)
                desencriptado = desencriptado + ABC[i]
            else:
                i = element
                desencriptado = desencriptado + i
        print(desencriptado)
    else:
        print("ERROR EN CLAVE")

desencripta(s, clave)