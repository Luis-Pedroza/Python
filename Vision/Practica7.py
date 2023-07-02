# -*- coding: utf-8 -*-
# ***************************************************
# ARCHIVO: Practica7.py
#
# DESCRIPCIÓN: 
# Detección de piel
#
# AUTOR:  Luis Pedroza
# REVISADO: 02/07/2023
# ******************* ********************************
import matplotlib.pyplot as plt
import numpy as np
import cv2

def SkinDetection(image, xSize, ySize):
    # Abrir imagen, modificar el tamaño y convertir a tipo float
    img = cv2.imread(image)
    original = cv2.resize(img,(xSize, ySize))
    original = np.array(original,dtype=float)
    [l,m,n] = original.shape

    # Crear matrices con ceros
    gris = np.zeros((l,m))
    corrector = np.zeros((l,m,n))
    umbral = np.zeros((l,m))
    segmento = np.zeros((l,m,n))
    mascara = np.zeros((l,m,n))

    # Aplicación de corrección gamma      
    corrector = pow((original/255),0.5)*255

    for i in range(l):
        for j in range(m):
            # Conversion a escala de grises
            gris[i][j] = corrector[i][j][0]*0.114 + corrector[i][j][1]*0.587 + corrector[i][j][2]*0.299
            # Aplicación del umbral
            if(gris[i][j] < 240 and gris[i][j] >= 170):
                umbral[i][j] = 255
            else:
                umbral[i][j] = 0

    # Segmentación de imagen        
    for i in range(l):
        for j in range(m):
            r, g, b = corrector[i][j]          
            val = max(r, g, b) - min(r, g, b)
            if r > 95 and g > 40 and b > 20 and val > 15:
                segmento[i][j] = corrector[i][j]
                mascara[i][j] = corrector[i][j]
                
    # aplicación de mascara            
    for i in range(l):
        for j in range(m):
            if umbral[i][j] ==  0:
                mascara[i][j] = 0

    # conversion a uint8
    original = np.array(original, dtype=np.uint8)
    gris = np.array(gris, dtype=np.uint8)
    corrector = np.array(corrector, dtype=np.uint8)
    umbral = np.array(umbral, dtype=np.uint8)
    segmento = np.array(segmento, dtype=np.uint8)
    mascara = np.array(mascara, dtype=np.uint8)

    # Mostrar imágenes
    cv2.imshow('Original', original)
    cv2.imshow('Corrección gamma', corrector)
    cv2.imshow('Gris', gris)
    cv2.imshow('Umbral', umbral)
    cv2.imshow('Segmentación', segmento)
    cv2.imshow('Final', mascara)

    # Mostrar el histograma
    histograma = cv2.calcHist([corrector], [0], None, [256], [0, 256])
    plt.stem(histograma)
    plt.title('Histograma')
    plt.xlabel('Valor de píxel')
    plt.ylabel('Frecuencia')
    plt.show()

    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    image = 'rosa.png'
    xSize = 334
    ySize = 467
    SkinDetection(image, xSize, ySize)