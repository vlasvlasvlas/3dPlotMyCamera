import cv2
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import time

# Inicializamos la cámara
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_BRIGHTNESS, 135)

if not cap.isOpened():
    print("No se puede abrir la cámara")
    exit()

# Activamos el modo interactivo de matplotlib
plt.ion() 

# Creamos una figura para Matplotlib
fig = plt.figure(figsize=(15, 15))
ax = fig.add_subplot(111, projection='3d')

# Preparamos las matrices de malla una sola vez para optimizar
X = np.arange(0, 640)  # Asumiendo resolución horizontal de 640
Y = np.arange(0, 480)  # Asumiendo resolución vertical de 480
X, Y = np.meshgrid(X, Y)

# Variables para controlar los ángulos
elevation = 90
azimuth = -90
elevation_step = 1
azimuth_step = 1



try:
    while True:
        ret, frame = cap.read()
        if ret:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            rotated = cv2.rotate(gray, cv2.ROTATE_180)
            brightened = np.clip(rotated + 10, 0, 255).astype(np.uint8)

            ax.clear()  # Limpiamos el gráfico para evitar ralentización
            # Personalización del gráfico para eliminar fondo y etiquetas

            # Ajustamos la posición y el tamaño del gráfico dentro de la figura
            ax.set_position([0, 0, 1, 1])

            ax.grid(False)  # Desactivamos la cuadrícula
            ax.set_xticks([])  # Eliminamos las marcas en x
            ax.set_yticks([])  # Eliminamos las marcas en y
            ax.set_zticks([])  # Eliminamos las marcas en z
            ax.axis('off')  # Desactivamos los ejes
            surf = ax.plot_surface(X, Y, brightened, cmap='viridis', edgecolor='none')
            ax.set_xlim(0, 640)
            ax.set_ylim(0, 480)
            ax.set_zlim(0, 255)

            ax.view_init(elevation, azimuth)
            elevation += elevation_step
            azimuth += azimuth_step

            if elevation >= 140 or elevation <= 40:
                elevation_step *= -1

            if azimuth >= -40 or azimuth <= -140:
                azimuth_step *= -1

            plt.draw()
            plt.pause(0.001)  # Pausa mínima para permitir redibujo
        else:
            print("No se pudo capturar el frame de la cámara")
            break
except KeyboardInterrupt:
    print("Detenido por el usuario")

cap.release()
plt.close()
