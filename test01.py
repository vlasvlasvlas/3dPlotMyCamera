import cv2
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Inicializamos la cámara
cap = cv2.VideoCapture(0)

# Intentamos ajustar el brillo de la cámara
cap.set(cv2.CAP_PROP_BRIGHTNESS, 150)

# Checamos si la cámara se ha inicializado correctamente
if not cap.isOpened():
    print("No se puede abrir la cámara")
    exit()

# Capturamos un frame de la cámara
ret, frame = cap.read()

# Si se capturó correctamente el frame
if ret:
    # Convertimos la imagen a escala de grises
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Rotamos la imagen 180 grados
    rotated = cv2.rotate(gray, cv2.ROTATE_180)

    # Ajustamos el brillo de la imagen
    brightened = np.clip(rotated + 15, 0, 255).astype(np.uint8)

    # Convertimos la imagen ajustada en blanco y negro a un DataFrame
    df_brightened = pd.DataFrame(brightened)
    
    # Guardamos el DataFrame en un archivo CSV sin encabezado
    df_brightened.to_csv('imagen_blanco_y_negro_brillante.csv', index=False, header=False)
    
    # Cerramos las ventanas de OpenCV
    cv2.destroyAllWindows()

    # Plot en 3D como un gráfico de superficie
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    X = np.arange(brightened.shape[1])
    Y = np.arange(brightened.shape[0])
    X, Y = np.meshgrid(X, Y)
    Z = brightened

    # Plot de la superficie
    surf = ax.plot_surface(X, Y, Z, cmap='gray', edgecolor='none')
    ax.view_init(75, -75)  # Vista cenital
    ax.set_title('Gráfico de Superficie en Escala de Grises')
    ax.axis('off')  # Ocultamos los ejes para una vista más clara
    plt.show()

    print("Imagen guardada y convertida a CSV y visualizada como gráfico de superficie.")
else:
    print("No se pudo capturar el frame de la cámara")

# Liberamos la cámara
cap.release()
