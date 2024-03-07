#El programa fuerza_bruta.py debe intentar todas las combinaciones de letras posibles, en
#orden alfabético, hasta que la combinación de letras sea igual a la de la contraseña indicada.
#Deberá hacer este proceso letra por letra, de izquierda a derecha.
#Simplificado
#Importación de Biblioteca
from string import ascii_lowercase

print("Bienvenido al programa de fuerza bruta para contraseñas.")

# Solicitar al usuario que ingrese la contraseña
contrasena = input("Ingresa la contraseña, sin espacios ni ñ: ").strip().lower()

# Inicializar variables
intentos = 0
combinacion_actual = ""

# Iterar a través de todas las combinaciones posibles
for caracter in contrasena:
    for caracter_comparativo in ascii_lowercase:
        intentos += 1
        if caracter == caracter_comparativo:
            combinacion_actual = ''.join(caracter)
            break

    if combinacion_actual == contrasena:
        break

print(f"Se adivinó la contraseña en {intentos} intentos.")