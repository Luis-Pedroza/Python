# ***************************************************
# ARCHIVO: Practica4.py
#
# DESCRIPCIÓN: 
# Corrección Gamma: Funciones de aclarado y oscurecimiento de imágenes
#
# AUTOR:  Luis Pedroza
# REVISADO: 05/06/2023
# ******************* ********************************

import numpy as np
import cv2

# Abrir imagen, modificar el tamaño y convertir a tipo float
img1 = cv2.imread('girl.png')
original = cv2.resize(img1,(640,802))
original = np.array(original,dtype=float)
[l,m,n] = original.shape

# Creación de matrices vacías
gris = np.zeros((l,m,n))
nuevaGris = np.zeros((l,m,n))


for i in range(l):
    for j in range(m):
        # Conversion a escala de grises
        gris[i][j] = original[i][j][0]*0.114 + original[i][j][1]*0.587 + original[i][j][2]*0.299
      
# Aplicación de corrección gamma      
nuevaGris = pow((gris/255),0.5)*255

# Conversion de matrices a uint8 
original = np.array(original, dtype=np.uint8)
gris = np.array(gris, dtype=np.uint8)
nuevaGris = np.array(nuevaGris, dtype=np.uint8)

# Mostrar imágenes
cv2.imshow('original', original)
cv2.imshow('gris', gris)
cv2.imshow('Corrección Gamma', nuevaGris)
cv2.waitKey(0)
cv2.destroyAllWindows()