

# Repositorio de Pruebas de Scripts

# Script de Visualización 3D en Tiempo Real con OpenCV y Matplotlib

Este script de Python utiliza OpenCV y Matplotlib para capturar imágenes en tiempo real desde una cámara, procesarlas y visualizarlas en un gráfico 3D en una ventana interactiva.

Este repositorio contiene una serie de scripts de prueba diseñados para diversas aplicaciones y casos de uso. Cada script se encuentra en un archivo separado y puede ejecutarse de forma independiente.

## Requisitos

Para ejecutar los scripts en este repositorio, se recomienda seguir estos pasos:

1. Clonar o descargar este repositorio en tu sistema local.
2. Crear un entorno virtual (venv) para instalar las dependencias de cada script y mantenerlas aisladas del sistema.

   ```bash
   python3 -m venv myenv
   ```

3. Activar el entorno virtual. Desde la terminal:

   - En Windows:

     ```bash
     myenv\Scripts\activate
     ```

   - En macOS y Linux:

     ```bash
     source myenv/bin/activate
     ```

4. Instalar las dependencias de cada script desde su respectivo archivo `requirements.txt`:

   ```bash
   pip install -r script_name/requirements.txt
   ```

   Sustituye `script_name` por el nombre del directorio del script que estés utilizando.

## Ejecución

Una vez que el entorno virtual esté activado y las dependencias estén instaladas, puedes ejecutar cada script por separado:

1. Clona o descarga este repositorio.
2. Ejecuta el script `test04.py`.
3. Ajusta la cámara para obtener la mejor visualización.
4. Observa la visualización 3D en tiempo real de los datos de la cámara.

Sustituye `script_name` por el nombre del directorio y el archivo del script que desees ejecutar.

## Descripción

El script realiza los siguientes pasos:

1. Inicializa la cámara utilizando OpenCV.
2. Crea una figura 3D utilizando Matplotlib.
3. Dentro de un bucle infinito:
    - Captura un fotograma de la cámara.
    - Convierte la imagen a escala de grises.
    - Rota la imagen 180 grados.
    - Ajusta el brillo de la imagen.
    - Limpia y actualiza el gráfico 3D con la nueva imagen procesada.
    - Controla la elevación y el azimut del gráfico para una rotación suave.
    - Dibuja y actualiza la ventana de visualización.


## Pruebas Anteriores

Si hay pruebas anteriores en el repositorio, puedes ejecutarlas de manera similar, sustituyendo `script_name` por el nombre del directorio y el archivo de la prueba anterior.

## Contribuciones

Si deseas contribuir con nuevos scripts de prueba o mejorar los existentes, ¡siéntete libre de hacerlo! Abre un problema o envía una solicitud de extracción con tus cambios.

## Licencia

Este repositorio está bajo la Licencia MIT. Consulta el archivo LICENSE para obtener más información.


## Notas

- El script utiliza el modo interactivo de Matplotlib para actualizar la visualización en tiempo real.
- Se supone que la cámara tiene una resolución de 640x480 píxeles.
- El script puede detenerse presionando Ctrl+C.