# Meta-1.3-Identificar-los-m-todos-usados-en-colecciones-y-Strings
Meta 1.3 Vara Andrea
1. Borrar Números en string. Diseña una función que entre un string y devuelve el string pero sin sus caracteres numéricos o dígitos. 
>>> delNumbers('Alicante a 20 kms')
 'Alicante a kms' 
 
2. Contar Mayusculas y minusculas. Diseña una función que cuente el número de mayúsculas y minúsculas de un texto que entra como un string. 
>>> contarMm('Hola') 
(1, 3) 
>>> contarMm('Ella dijo: HOLA') 
(5, 7)

3. Encriptar. Diseñe una función encripta(s, clave), que reciba un string s con un mensaje y un string con una clave de codificación, y retorne el mensaje codificado según la clave leída. Los signos de puntuación y dígitos que aparezcan en el mensaje deben conservarse sin cambios. La clave consiste en una sucesión de las 26 letras minúsculas del alfabeto, las cuales se hacen corresponder con el alfabeto básico (a…z, sin la ñ o vocales acentuadas) de 26 letras. La primera letra de la clave se relaciona con la letra 'a', la segunda con la letra 'b', etc. Por ejemplo, una entrada de la forma: 
Clave = 'ixmrklstnuzbowfaqejdcpvhyg' 
Texto para codificar: 'cafe
Con esta clave la letra 'i' se corresponde con la letra 'a', la letra 'x' se corresponde con la letra 'b', la letra 'm' se corresponde con la letra 'c', y así sucesivamente, por lo que el ejemplo anterior debería dar como salida: 'milk'. 
Nota: para simplificar consideraremos solo mensajes de entrada en minúsculas. 
>>> encripta('cafe', ' ixmrklstnuzbowfaqejdcpvhyg') 
'milk' 
>>> encripta('dame 1 chocolate', ' ixmrklstnuzbowfaqejdcpvhyg') 
'riok 1 mtfmfbidk'

4. Desencriptar. Diseña una función desencripta(s, clave) que realice la función inversa a la función anterior, es decir, reciba un string s y una clave y realice la desencriptación del mensaje en el string devolviendo la cadena desencriptada. 
>>> clave = ' ixmrklstnuzbowfaqejdcpvhyg' 
>>> desencripta('milk',clave)
 'cafe' 
>>> desencripta('riok 1 mtfmfbidk',clave) 
'dame 1 chocolate'

5. Números sin repetir. Escribe la función uniqueNumbers() usando la estructura while que lea números enteros del teclado hasta que obtenga 5 números distintos (no repetidos) y devuelva una lista con estos números distintos. 
Ejemplos: 
El usuario introduce: 
0 (primer número) 
4 (segundo número) 
5 (tercer número) 
4 (Repetido,no se cuenta ni se pone en la lista) 
5 (Repetido,no se cuenta ni se pone en la lista)
3 (cuarto número) 
6 (es el quinto número diferente y el último) 
La función devuelve la lista de números [0, 4, 5, 3, 6]

6. Positivos y Negativos. Diseña una función PositNegat(lst) que reciba una lista, lst, y devuelva 2 listas, una con los Valores positivos o 0 y otra con los negativos. 
>>> PositNegat([69, -37, 0, -27, -59, 83, 1, 45]) 
([69, 0, 83, 1, 45], [-37, -27, -59]) 
>>> PositNegat([3, 4, 7, 12]) 
([3, 4, 7, 12], [])

7. Mover elementos de una lista a la derecha (Right shift). Diseña una función mueve_derecha(lst) (no productiva) que dada una lista, lst, la devuelva con sus elementos corridos hacia la derecha (y el último de primero). Right-shift. 
>>> lst = [2, 4, 6, 8, 10] 
>>> mueve_derecha(lst) 
>>> lst 
[10, 2, 4, 6, 8] 

8. Media de cada fila. Diseña una función media_filas(lst) que, dada una lista de listas, que representa una matriz (los elementos de la lista son las filas de la matriz), de nf filas y nc columnas, devuelva una lista con el cálculo del valor medio de cada fila. Ejemplo: 
>>> lst = [[1,2,3,4],[1,3,5,7]
 >>> media_filas(lst) 
[2.5, 4.0]

9. Frecuencia de Números. Diseña una función frecuencias(lst) en que, dada una lista de números naturales, devuelve un diccionario con el número de veces que aparece cada número en la lista dada. 
>>> frecuencias([1, 3, 2, 4, 2, 2, 3, 2, 4, 1, 2, 1, 2, 3, 1, 3, 1]) 
{1: 5, 2: 6, 3: 4, 4: 2}

10. Temperaturas de ciudades. Un diccionario guarda las temperaturas mínimas de los 3 primeros meses del año de distintas ciudades, de la forma: 
dic = {'Londres': [3.4, 6.3, 10.5], 'Oslo': [-3.8, -5.0, 4.2], 'Rennes': [2.5, 3.1, 12.3]}
Diseña una función mediaTemp(dict), en que dado un diccionario como el del ejemplo nos devuelva un diccionario con el valor medio de las temperaturas de cada ciudad (redondear a 2 decimales). Ejemplo: 
>>> mediaTemp(dic) 
{'Londres': 6.73, 'Rennes': 5.97, 'Oslo': -1.53}
Diseña una función minimasTemp(dict), en que dado un diccionario como el del ejemplo nos devuelva un diccionario con el valor mínimo de las temperaturas de cada ciudad. Ejemplo: 
>>> minimasTemp(dic) 
{'Londres': 3.4, 'Rennes': 2.5, 'Oslo': -5.0}
Diseña una función minTemp(dict), en que dado un diccionario como el del ejemplo nos devuelva una lista con la ciudad con la temperatura más baja y su valor. Ejemplo: 
>>> minTemp(dic) 
['Oslo', -5.0
