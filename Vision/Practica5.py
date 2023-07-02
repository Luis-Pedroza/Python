# ***************************************************
# ARCHIVO: Practica5.py
#
# DESCRIPCIÓN: 
# Operadores detectores de bordes
#
# AUTOR:  Luis Pedroza
# REVISADO: 02/07/2023
# ****************************************************
import cv2
import numpy as np

# Abrir imagen y cambiar a escala de grises
original = cv2.imread('mario.png')
gris = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)

# Mascara
mascara=np.array([[0,1,0],
                  [1,-4,1],
                  [0,1,0]])

# Filtro
bordes=cv2.filter2D(gris,0,mascara)

# Conversion a uint8
gris = np.array(gris, dtype=np.uint8)
bordes = np.array(bordes, dtype=np.uint8)

# Mostrar imágenes
cv2.imshow('Gris', gris)
cv2.imshow('Bordes', bordes)
cv2.waitKey(0)
cv2.destroyAllWindows()