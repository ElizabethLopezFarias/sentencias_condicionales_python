print("¡Bienvenido a la aplicación de primeros auxilios!")

# Pregunta inicial
while True:
    respuesta_estimulos = input("¿Responde a estímulos? (SI/NO): ").strip().lower()
    if respuesta_estimulos in ("si", "no"):
        break
    else:
        print("Respuesta inválida. Por favor, ingresa 'SI' o 'NO'.")

if respuesta_estimulos == "si":
    print("Valoren la necesidad de llevarlo al hospital más cercano.")
elif respuesta_estimulos == "no":
    print("Abrir la Vía Aérea y verificar si respira.")
    while True:
        respuesta_respira = input("¿Respira? (SI/NO): ").strip().lower()
        if respuesta_respira in ("si", "no"):
            break
        else:
            print("Respuesta inválida. Por favor, ingresa 'SI' o 'NO'.")

    if respuesta_respira == "si":
        print("Permitirle posición de suficiente ventilación.")
    elif respuesta_respira == "no":
        print("Administrar 5 ventilaciones y llamar a la ambulancia.")
        print("Luego, checar los signos de vida.")
        while True:
            respuesta_signos_vitales = input("¿Tiene signos vitales? (SI/NO): ").strip().lower()
            if respuesta_signos_vitales in ("si", "no"):
                break
            else:
                print("Respuesta inválida. Por favor, ingresa 'SI' o 'NO'.")

        if respuesta_signos_vitales == "si":
            print("Reevaluar a la espera de la ambulancia.")
        elif respuesta_signos_vitales == "no":
            print("Administrar 5 Compresiones Torácicas")
            while True:
                llego_ambulancia = input("¿Llegó la ambulancia? (SI/NO): ").strip().lower()
                if llego_ambulancia in ("si", "no"):
                    break
                else:
                    print("Respuesta inválida. Por favor, ingresa 'SI' o 'NO'.")

            if llego_ambulancia == "si":
                print("Esperemos que todo salga bien.")
            elif llego_ambulancia == "no":
                print("Administrar 5 Compresiones Torácicas hasta que llegue la ambulancia.")
            else:
                print("Respuesta inválida. Por favor, ingresa 'SI' o 'NO'.")
else:
    print("Respuesta inválida. Por favor, ingresa 'SI' o 'NO'.")