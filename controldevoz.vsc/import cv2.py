import cv2
import keyboard

def controlar_volumen(subir):
    if subir:
        keyboard.press('up')
    else:
        keyboard.press('down')

# Cargar el clasificador de reconocimiento facial de OpenCV
cascada_cara = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Iniciar la cámara
camara = cv2.VideoCapture(0)

while True:
    # Leer el fotograma actual de la cámara
    _, fotograma = camara.read()

    # Convertir a escala de grises para el procesamiento
    gris = cv2.cvtColor(fotograma, cv2.COLOR_BGR2GRAY)

    # Detectar caras en el fotograma
    caras = cascada_cara.detectMultiScale(gris, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Controlar el volumen basado en la detección de caras
    if len(caras) > 0:
        # Subir volumen si se detecta una cara
        controlar_volumen(subir=True)
    else:
        # Bajar volumen si no se detecta una cara
        controlar_volumen(subir=False)

    # Mostrar el fotograma con las caras detectadas
    for (x, y, w, h) in caras:
        cv2.rectangle(fotograma, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Mostrar el fotograma en una ventana
    cv2.imshow('Reconocimiento Facial', fotograma)

    # Salir del bucle si se presiona la tecla 'q'
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
