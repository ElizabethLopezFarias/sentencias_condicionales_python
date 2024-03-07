#El programa fuerza_bruta.py debe intentar todas las combinaciones de letras posibles, en
#orden alfabético, hasta que la combinación de letras sea igual a la de la contraseña indicada.
#Deberá hacer este proceso letra por letra, de izquierda a derecha.

#Importación de Bibliotecas
from string import ascii_lowercase #contiene todas las letras minúsculas del alfabeto inglés
from itertools import product #realiza el producto cartesiano de los iterables proporcionados
import getpass # proporciona una forma segura de ingresar contraseñas sin mostrar la entrada en pantalla

print("Bienvenido al programa de fuerza bruta para contraseñas.")

# Solicitar al usuario que ingrese la contraseña y la oculta
contrasena_oculta = getpass.getpass("Ingresa la contraseña (sin la ñ): ")

# Convertir la contraseña a minúsculas
contrasena_oculta = contrasena_oculta.lower()

# Inicializar variables
intentos = 0
combinacion_actual = ""

# Obtener la longitud de la contraseña
longitud_contrasena = len(contrasena_oculta)

# Iterar a través de todas las combinaciones posibles
# La función product genera todas las combinaciones posibles de letras minúsculas con la longitud especificada. 

for combinacion in product(ascii_lowercase, repeat=longitud_contrasena):
    intentos += 1
    combinacion_actual = ''.join(combinacion) #une la cadena de caracteres para ir comparando la cadena ingresada con la comparativa

    if combinacion_actual == contrasena_oculta:
        break

print(f"Se adivinó la contraseña en {intentos} intentos.")