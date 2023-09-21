import speech_recognition as sr
import webbrowser

# Inicializar el reconocimiento de voz
r = sr.Recognizer()

# Función para capturar y procesar el comando de voz
def procesar_comando():
    with sr.Microphone() as source:
        print("Di algo...")
        audio = r.listen(source)

    try:
        # Utilizar Google Speech Recognition para convertir el audio en texto
        texto = r.recognize_google(audio, language='es')
        print("Has dicho: " + texto)
        
        # Verificar si el comando es "abrir YouTube"
        if "Abrir YouTube" in texto:
            # Abrir YouTube en el navegador
            webbrowser.open("https://www.youtube.com")
           
             # Verificar si el comando es "abrir Google"
        if "Abrir Google" in texto:
            # Abrir Google en el navegador
            webbrowser.open("https://www.google.com")

  # Verificar si el comando es "abrir Google"
        if "Abrir Google" in texto:
            # Abrir Google en el navegador
            webbrowser.open("https://www.google.com")


        # Verificar si el comando es "Cerrar asistente"
        if "cerrar asistente" in texto:
            # Detener el asistente y salir del bucle
            print("Cerrando asistente...")
            return True
        
        # Verificar si el comando es "abrir fútbol"
        if "abrir fútbol" in texto:
            # Abrir Google en el navegador
            webbrowser.open("https://www.haxball.com/")


    except sr.UnknownValueError:
        print("No se pudo reconocer el audio")

    except sr.RequestError as e:
        print("Error al obtener resultados del servicio de reconocimiento de voz; {0}".format(e))

    return False

# Ejecutar el procesamiento del comando de voz continuamente
while True:
    if procesar_comando():
        break
