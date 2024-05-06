import cv2
import numpy as np

def nothing(x):
    pass

# Crear una ventana para los controles deslizantes de HSV
cv2.namedWindow("HSV Adjustments")
cv2.createTrackbar("Low H", "HSV Adjustments", 9, 179, nothing)
cv2.createTrackbar("High H", "HSV Adjustments", 179, 179, nothing)
cv2.createTrackbar("Low S", "HSV Adjustments", 135, 255, nothing)
cv2.createTrackbar("High S", "HSV Adjustments", 255, 255, nothing)
cv2.createTrackbar("Low V", "HSV Adjustments", 116, 255, nothing)
cv2.createTrackbar("High V", "HSV Adjustments", 255, 255, nothing)

# Inicializar la captura de video desde la webcam
cap = cv2.VideoCapture(0)

# Crear un fondo para el efecto de "dibujo"
fondo = None
last_center = None

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Convertir el frame a espacio de color HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Leer valores de los controles deslizantes
    low_h = cv2.getTrackbarPos("Low H", "HSV Adjustments")
    high_h = cv2.getTrackbarPos("High H", "HSV Adjustments")
    low_s = cv2.getTrackbarPos("Low S", "HSV Adjustments")
    high_s = cv2.getTrackbarPos("High S", "HSV Adjustments")
    low_v = cv2.getTrackbarPos("Low V", "HSV Adjustments")
    high_v = cv2.getTrackbarPos("High V", "HSV Adjustments")

    # Crear una máscara con los valores HSV ajustados
    lower_hsv = np.array([low_h, low_s, low_v])
    upper_hsv = np.array([high_h, high_s, high_v])
    mask = cv2.inRange(hsv, lower_hsv, upper_hsv)

    # Encontrar contornos en la máscara
    contornos, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if fondo is None:
        fondo = np.zeros_like(frame)

    for contorno in contornos:
        # Obtener el centro y el radio del círculo que envuelve cada contorno
        (x, y), radio = cv2.minEnclosingCircle(contorno)
        centro = (int(x), int(y))
        radio = int(radio)

        if radio > 10:
            if last_center is not None:
                # Dibujar una línea desde el último centro hasta el centro actual
                cv2.line(fondo, last_center, centro, (10, 10, 255), 10)
            last_center = centro

    # Ajustar la velocidad a la que se desvanece el trazo
    fondo = cv2.addWeighted(fondo, 0.98, np.zeros_like(frame), 0.02, 0)
    resultado = cv2.addWeighted(frame, 1, fondo, 1, 0)

    cv2.imshow('Dibujo con Pelota de Tenis', resultado)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()