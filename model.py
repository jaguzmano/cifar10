import numpy as np
from PIL import Image
from keras.models import load_model

modelo = load_model('modelo_densenet.h5')

nombres_clases_cifar10 = ["Avión", "Automóvil", "Pájaro", "Gato", "Ciervo", "Perro", "Rana", "Caballo", "Barco", "Camión"]

def clasificar_imagen(imagen):
    imagen = procesar_imagen(imagen)
    resultado_index = clasificar_con_modelo(imagen)
    resultado_clase = nombres_clases_cifar10[resultado_index]
    return resultado_clase

def procesar_imagen(imagen):
    imagen = Image.open(imagen)
    imagen = imagen.resize((32, 32))
    imagen = np.array(imagen)
    imagen = imagen / 255.0
    imagen = imagen.reshape(1, 32, 32, 3)  # 3 canales para imágenes a color
    return imagen

def clasificar_con_modelo(imagen):
    resultado = modelo.predict(imagen)
    clasificacion = np.argmax(resultado)
    return clasificacion
