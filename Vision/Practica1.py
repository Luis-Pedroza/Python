# ***************************************************
# ARCHIVO: Practica1.py
#
# DESCRIPCIÓN: 
# Transformaciones espaciales y operaciones con imágenes
#
# AUTOR:  Luis Pedroza
# REVISADO: 05/06/2023
# ******************* ********************************

import numpy as np
import cv2

# Abrir imagen
img1 = cv2.imread('girl.png')
img2= cv2.imread('house.jpg')

# Cambiar tamaño de imágenes
original1 = cv2.resize(img1,(640,802))
original2 = cv2.resize(img2,(640,802))

# Obtener tamaño de imagines
[l,m,n] = original1.shape

# Declaración de matrices vacías
suma = np.zeros((l,m,n))
resta = np.zeros((l,m,n))
multi = np.zeros((l,m,n))
refVer = np.zeros((l,m,n))
refHor = np.zeros((l,m,n))

# Conversion de matrices originales a tipo float
original1 = np.array(original1,dtype=float)
original2 = np.array(original2,dtype=float)


for i in range(l):
    for j in range(m):
        for k in range(n):
            # suma
            var = original1[i][j][k] + original2[i][j][k]
            if var > 255:
                suma[i][j][k] = 255
            else:
                suma[i][j][k] = original1[i][j][k] + original2[i][j][k]
            # Resta
            resta[i][j][k] = abs(original1[i][j][k] - original2[i][j][k])
            # Multiplicación
            multi[i][j][k] = (original1[i][j][k] * original2[i][j][k])/255
            # Reflejos
            refVer[i][j][k] = original1[-i][j][k]
            refHor[i][j][k] = original1[i][-j][k]
            
# Conversion de matrices a uint8            
suma = np.array(suma, dtype=np.uint8)
resta = np.array(resta, dtype=np.uint8)
multi = np.array(multi, dtype=np.uint8)
refVer = np.array(refVer, dtype=np.uint8)
refHor = np.array(refHor, dtype=np.uint8)

# Mostrar todas las imágenes
cv2.imshow('Suma', suma)
cv2.imshow('Resta', resta)
cv2.imshow('Multiplicación', multi)
cv2.imshow('Reflejo Horizontal', refVer)
cv2.imshow('Reflejo Vertical', refHor)
cv2.waitKey(0)
cv2.destroyAllWindows()