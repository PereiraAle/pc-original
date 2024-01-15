import cv2
import keyboard

def controlar_volumen(subir):
    if subir:
        keyboard.press('up')
    else:
        keyboard.press('down')


cascada_cara = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


camara = cv2.VideoCapture(0)

while True:
   
    _, fotograma = camara.read()

   
    gris = cv2.cvtColor(fotograma, cv2.COLOR_BGR2GRAY)

   
    caras = cascada_cara.detectMultiScale(gris, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

   
    if len(caras) > 0:
      
        controlar_volumen(subir=True)
    else:
     
        controlar_volumen(subir=False)

   
    for (x, y, w, h) in caras:
        cv2.rectangle(fotograma, (x, y), (x+w, y+h), (0, 255, 0), 2)

   
    cv2.imshow('Reconocimiento Facial', fotograma)

    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    import cv2

camara = cv2.VideoCapture(0)

while True:
    _, fotograma = camara.read()
    cv2.imshow('Cámara', fotograma)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

camara.release()
cv2.destroyAllWindows()


# Liberar la cámara y cerrar las ventanas
camara.release()
cv2.destroyAllWindows()
