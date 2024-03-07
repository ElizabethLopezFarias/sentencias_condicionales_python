#Aplicación interactiva primeros_auxilios.py que entrega los distintos pasos a seguir dependiendo de las respuestas que el usuario entrega
#en tiempo real en caso de una emergencia médica 

print("¡Bienvenido a la aplicación de primeros auxilios!")

# Pregunta si Responde a estímulos, si la respuesta no es válida, la vuelve a consultar
# .strip() elimina los espacios .lower() convierte a minúsculas
while True:
    respuesta_estimulos = input("¿Responde a estímulos? (SI/NO): ").strip().lower()
    if respuesta_estimulos in ("si", "no"):
        break
    else:
        print("Respuesta inválida. Por favor, ingresa 'SI' o 'NO'.")

if respuesta_estimulos == "si":
    print("Valoren la necesidad de llevarlo al hospital más cercano.")

#entrega instrucciones si no responde a estímulos
elif respuesta_estimulos == "no":
    print("Abrir la Vía Aérea y verificar si respira.")
    # Pregunta si Respira
    while True:
        respuesta_respira = input("¿Respira? (SI/NO): ").strip().lower()
        if respuesta_respira in ("si", "no"):
            break
        else:
            print("Respuesta inválida. Por favor, ingresa 'SI' o 'NO'.")
    #entrega indicaciones dependiendo de la respuesta
    if respuesta_respira == "si":
        print("Permitirle posición de suficiente ventilación.")
    elif respuesta_respira == "no":
        print("Administrar 5 ventilaciones y llamar a la ambulancia.")
        print("Luego, checar los signos de vida.")
        #Pregunta si tiene signos vitales y verifica la respuesta para que sea válida
        while True:
            respuesta_signos_vitales = input("¿Tiene signos vitales? (SI/NO): ").strip().lower()
            if respuesta_signos_vitales in ("si", "no"):
                break
            else:
                print("Respuesta inválida. Por favor, ingresa 'SI' o 'NO'.")
        if respuesta_signos_vitales == "si":
            print("Reevaluar a la espera de la ambulancia, mantenga la calma.")
        elif respuesta_signos_vitales == "no":
            print("Mantenga la calma y administre 5 Compresiones Torácicas más. mientras sige esperando")
            while True:
                llego_ambulancia = input("¿Llegó la ambulancia? (SI/NO): ").strip().lower()
                if llego_ambulancia in ("si", "no"):
                    break
                else:
                    print("Respuesta inválida. Por favor, ingresa 'SI' o 'NO'.")

            if llego_ambulancia == "si":
                print("Esperemos que todo salga bien.")
            #Repite si la respuesta es negativa
            elif llego_ambulancia == "no":
                print("Administrar 5 Compresiones Torácicas hasta que llegue la ambulancia.")
            else:
                print("Respuesta inválida. Por favor, ingresa 'SI' o 'NO'.")
else:
    print("Respuesta inválida. Por favor, ingresa 'SI' o 'NO'.")