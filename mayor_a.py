# Diccionario de ventas
ventas = {
    "Enero": 15000,
    "Febrero": 22000,
    "Marzo": 12000,
    "Abril": 17000,
    "Mayo": 81000,
    "Junio": 13000,
    "Julio": 21000,
    "Agosto": 41200,
    "Septiembre": 25000,
    "Octubre": 21500,
    "Noviembre": 91000,
    "Diciembre": 21000,
}

# Umbral específico (por ejemplo, 20000)
umbral_str = input("Por favor, ingresa el valor del umbral: ")

#isdigit() para verificar si el valor 
if umbral_str.replace(".", "", 1).isdigit():
    umbral = float(umbral_str)
else:
    print("Error: Ingresa un valor numérico válido.")
    exit()

# Crear un diccionario para almacenar los meses que superan el umbral
meses_mayor_a_umbral = {}

# Iterar sobre el diccionario de ventas
for mes, valor in ventas.items():
    if valor > umbral:
        meses_mayor_a_umbral[mes] = valor

# Imprimir el resultado
print ("Los meses que superaron el umbral ingresado son los siguientes:")
for mes, valor in meses_mayor_a_umbral.items():
    print(f"{mes}: ${valor}")