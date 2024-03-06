from string import ascii_lowercase
from itertools import product
import getpass

print("Bienvenido al programa de fuerza bruta para contraseñas.")

# Solicitar al usuario que ingrese la contraseña y no la muestra al teclearla
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
    combinacion_actual = ''.join(combinacion)

    if combinacion_actual == contrasena_oculta:
        break

print(f"Se adivinó la contraseña en {intentos} intentos.")