# ***************************************************
# ARCHIVO: Practica2.py
#
# DESCRIPCIÓN: 
# Dispositivos RGB y obtención de los canales R, G y B de una imagen.
#
# AUTOR:  Luis Pedroza
# REVISADO: 05/06/2023
# ******************* ********************************

import numpy as np
import cv2

# Lectura de imagen
img1 = cv2.imread('girl.png')
original = cv2.resize(img1,(640,802))
[l,m,n] = original.shape

# Creación de matrices vacías
red = np.zeros((l,m,n))
green = np.zeros((l,m,n))
blue = np.zeros((l,m,n))

# Conversion de matriz a tipo float
original = np.array(original,dtype=float)

for i in range(l):
    for j in range(m):
        for k in range(n):
            # Obtención de las capas R, G y B.
            red[i][j][0] = original[i][j][k]
            green[i][j][1] = original[i][j][k]
            blue[i][j][2] = original[i][j][k]

# Conversion de matrices a uint8
original = np.array(original, dtype=np.uint8)
red = np.array(red, dtype=np.uint8)
green = np.array(green, dtype=np.uint8)
blue = np.array(blue, dtype=np.uint8)

# Mostrar imagenes
cv2.imshow('Original', original)
cv2.imshow('Blue', red)
cv2.imshow('Green', green)
cv2.imshow('Red', blue)
cv2.waitKey(0)
cv2.destroyAllWindows()