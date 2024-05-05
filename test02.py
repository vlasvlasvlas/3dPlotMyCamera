import cv2
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import time

# Inicializamos la cámara
cap = cv2.VideoCapture(0)

# Intentamos ajustar el brillo de la cámara
cap.set(cv2.CAP_PROP_BRIGHTNESS, 150)

# Checamos si la cámara se ha inicializado correctamente
if not cap.isOpened():
    print("No se puede abrir la cámara")
    exit()

# Activamos el modo interactivo de matplotlib
plt.ion()

# Creamos una figura para Matplotlib, especificando un tamaño más grande
fig = plt.figure(figsize=(12, 10))  # Aumentamos el tamaño de la figura
ax = fig.add_subplot(111, projection='3d')

try:
    while True:
        # Capturamos un frame de la cámara
        ret, frame = cap.read()

        # Si se capturó correctamente el frame
        if ret:
            # Convertimos la imagen a escala de grises
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            
            # Rotamos la imagen 180 grados
            rotated = cv2.rotate(gray, cv2.ROTATE_180)

            # Ajustamos el brillo de la imagen
            brightened = np.clip(rotated + 30, 0, 255).astype(np.uint8)

            # Guardamos la imagen ajustada en un DataFrame y lo exportamos a CSV sin encabezado
            df_brightened = pd.DataFrame(brightened)
            df_brightened.to_csv('imagen_blanco_y_negro_brillante.csv', index=False, header=False)

            # Configuramos los datos para el gráfico de superficie
            X = np.arange(brightened.shape[1])
            Y = np.arange(brightened.shape[0])
            X, Y = np.meshgrid(X, Y)
            Z = brightened

            # Limpiamos el gráfico anterior
            ax.clear()

            # Ajustamos la posición y el tamaño del gráfico dentro de la figura
            ax.set_position([0, 0, 1, 1])  # Esto maximiza el área del plot dentro de la figura

            # Plot de la superficie con más "zoom"
            surf = ax.plot_surface(X, Y, Z, cmap='inferno', edgecolor='none')
            ax.set_xlim(0, brightened.shape[1])  # Ajustamos los límites del eje X
            ax.set_ylim(0, brightened.shape[0])  # Ajustamos los límites del eje Y
            ax.set_zlim(0, 255)                  # Ajustamos los límites del eje Z
            ax.view_init(90, -90)  # Vista cenital
            ax.set_title('Gráfico de Superficie en Escala de Grises')
            ax.axis('off')  # Ocultamos los ejes para una vista más clara
            
            # Dibujamos y pausamos brevemente para la actualización
            plt.draw()
            plt.pause(0.001)
            
            # Esperamos 0.5 segundos antes de la próxima captura
            time.sleep(0.5)
        else:
            print("No se pudo capturar el frame de la cámara")
            break
except KeyboardInterrupt:
    print("Detenido por el usuario.")

# Liberamos la cámara y cerramos todas las ventanas
cap.release()
plt.close()
