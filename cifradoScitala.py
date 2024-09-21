#Programa de cifrado scitala con python 
#Para correrlo debemos entrar a una terminal y colocarnos en 
#   la direccion donde se encuentre el archivo posteriormente 
#   corremos el siguiente comando python3 cifradoScitala.py 


# Menú para seleccionar la opción de cifrar o descifrar
opcion = input("¿Qué deseas hacer con el mensaje? (cifrar o descifrar): ").lower()
mensaje = input("Dame el mensaje que deseas cifrar o descifrar: ")
num_columnas = int(input("Ingresa el número de columnas (clave): "))
mensaje_ingresado = mensaje
# #Prueba
# mensaje = "¡Hola diplomado de ciber seguridad generacion 16!"
# desplazamiento = 4


# Función para cifrar el mensaje usando Scítala
def cifrar_scitala(mensaje, num_columnas):
    # Eliminamos los espacios del mensaje
    mensaje = mensaje.replace(" ", "")
    
    # Calculamos el número de filas necesarias
    filas = len(mensaje) // num_columnas
    if len(mensaje) % num_columnas:
        filas += 1
    
    # Añadimos relleno si es necesario para completar la matriz
    relleno = filas * num_columnas - len(mensaje)
    mensaje += " " * relleno  # Relleno con espacios
    
    # Creamos una matriz vacía para la scítala
    matriz = [""] * filas
    
    # Rellenamos la matriz con el mensaje
    for i in range(len(mensaje)):
        fila = i % filas
        matriz[fila] += mensaje[i]
    
    # Unimos las columnas para formar el mensaje cifrado
    mensaje_cifrado = "".join(matriz).strip()
    return mensaje_cifrado

# Función para descifrar el mensaje usando Scítala
def descifrar_scitala(mensaje_cifrado, num_columnas):
    # Calculamos el número de filas
    filas = len(mensaje_cifrado) // num_columnas
    if len(mensaje_cifrado) % num_columnas:
        filas += 1
    
    # Añadimos relleno si es necesario
    relleno = filas * num_columnas - len(mensaje_cifrado)
    mensaje_cifrado += " " * relleno  # Relleno con espacios
    
    # Creamos una matriz vacía para la scítala
    matriz = [""] * num_columnas
    
    # Rellenamos la matriz con el mensaje cifrado
    for i in range(len(mensaje_cifrado)):
        columna = i % num_columnas
        matriz[columna] += mensaje_cifrado[i]
    
    # Unimos las filas para formar el mensaje descifrado
    mensaje_descifrado = "".join(matriz).strip()
    return mensaje_descifrado

# #Prueba
# Mensaje Cifrado: ¡aeeHdgrooualdrcaeiidcdoiianpbd1leg6ore!msn
# Mensaje Descifrado: ¡Holadiplomadodeciberseguridadgeneracion16!
# mensaje = "¡Hola diplomado de ciber seguridad generacion 16!"
# num_columnas = 4

if opcion == "cifrar":
    mensaje_cifrado = cifrar_scitala(mensaje, num_columnas)
    print("Mensaje Cifrado:", mensaje_cifrado)
    print("Mensaje ingresado:", mensaje_ingresado)
elif opcion == "descifrar":
    mensaje_descifrado = descifrar_scitala(mensaje, num_columnas)
    print("Mensaje Descifrado:", mensaje_descifrado)
    print("Mensaje ingresado:", mensaje_ingresado)
else:
    print("Error en la seleeción; Por favor, selecciona 'cifrar' o 'descifrar' ")

