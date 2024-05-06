import cv2
import numpy as np
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
fig = plt.figure(figsize=(15, 15))
ax = fig.add_subplot(111, projection='3d')

# Variables para controlar los ángulos
elevation = 90  # Elevación inicial
azimuth = -90   # Azimut inicial
elevation_step = 2  # Paso de elevación
azimuth_step = 2    # Paso de azimut

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
            brightened = np.clip(rotated + 10, 0, 255).astype(np.uint8)

            # Invertimos los valores de la imagen
            #inverted = 255 - brightened
            inverted = brightened

            # Configuramos los datos para el gráfico de superficie
            X = np.arange(inverted.shape[1])
            Y = np.arange(inverted.shape[0])
            X, Y = np.meshgrid(X, Y)
            Z = inverted

            # Limpiamos el gráfico anterior
            ax.clear()

            # Ajustamos la posición y el tamaño del gráfico dentro de la figura
            ax.set_position([0, 0, 1, 1])

            # Plot de la superficie sin bordes entre las celdas
            surf = ax.plot_surface(X, Y, Z, cmap='viridis', edgecolor='none')
            ax.set_xlim(0, inverted.shape[1])
            ax.set_ylim(0, inverted.shape[0])
            ax.set_zlim(0, 255)
            
            # Actualizamos los ángulos de vista
            ax.view_init(elevation, azimuth)
            elevation += elevation_step
            azimuth += azimuth_step
            
            # Invertimos la dirección si alcanzamos los límites
            if elevation >= 140 or elevation <= 40:
                elevation_step *= -1
            if azimuth >= -40 or azimuth <= -140:
                azimuth_step *= -1

            ax.axis('off')
            
            # Dibujamos y pausamos brevemente para la actualización
            plt.draw()
            plt.pause(0.001)
            
            # Esperamos 0.5 segundos antes de la próxima captura
            time.sleep(0.1)
        else:
            print("No se pudo capturar el frame de la cámara")
            break
except KeyboardInterrupt:
    print("Detenido por el usuario.")

# Liberamos la cámara y cerramos todas las ventanas
cap.release()
plt.close()
