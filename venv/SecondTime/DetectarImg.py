import numpy
import tensorflow as tf
import keras
from keras.preprocessing import image
from keras.applications.inception_v3 import InceptionV3, decode_predictions
#Creamos instancia
iv3 = InceptionV3()
#Cargamos imagen
#from google.colab import files
uploaded = files.upload()
x = image.img_to_array(image.load_img("edit final.png", target_size=(299, 289)))
#Creamos dimensiones
x = x.reshape([1, x.shape[0], x.shape[1], x.shape[2]])
#analizar la imagen con predict
keras.aplications.inception_v3.preprocess_input(x)
y = iv3.predict(x)
#mostrar resultado
print(decode_predictions(y))
#guardar predicción
datos1 = decode_predictions(y)
print("imagen 2 clasificada como:")
print(datos[0][0])