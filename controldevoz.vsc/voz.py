import speech_recognition as sr
import webbrowser


r = sr.Recognizer()

def procesar_comando():
    with sr.Microphone() as source:
        print("Di algo...")
        audio = r.listen(source)

    try:
      
        texto = r.recognize_google(audio, language='es')
        print("Has dicho: " + texto)
        
      
        if "Abrir YouTube" in texto:
         
            webbrowser.open("https://www.youtube.com")
           
        
        if "Abrir Google" in texto:
         
            webbrowser.open("https://www.google.com")


        if "Abrir Google" in texto:
       
            webbrowser.open("https://www.google.com")



        if "cerrar asistente" in texto:
      
            print("Cerrando asistente...")
            return True
        
   
        if "abrir fútbol" in texto:
         
            webbrowser.open("https://www.haxball.com/")


    except sr.UnknownValueError:
        print("No se pudo reconocer el audio")

    except sr.RequestError as e:
        print("Error al obtener resultados del servicio de reconocimiento de voz; {0}".format(e))

    return False


while True:
    if procesar_comando():
        break
