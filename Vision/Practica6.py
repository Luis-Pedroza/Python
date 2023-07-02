# ***************************************************
# ARCHIVO: Practica6.py
#
# DESCRIPCIÓN: 
# Operadores puntuales
#
# AUTOR:  Luis Pedroza
# REVISADO: 02/07/2023
# ****************************************************
import matplotlib.pyplot as plt
import numpy as np
import cv2

img1 = cv2.imread('Mario.png')
original = cv2.resize(img1,(668,850))
original = np.array(original,dtype=float)
[l,m,n] = original.shape

gris = np.zeros((l,m))
identidad = np.zeros((l,m))
inverso = np.zeros((l,m))
umbral = np.zeros((l,m))
Ubinario = np.zeros((l,m))
UBinvertido = np.zeros((l,m))
UescalaG = np.zeros((l,m))
UEGinvertido = np.zeros((l,m))

lista=np.zeros([256])
for i in range(l):
    for j in range(m):
        gris[i][j] = original[i][j][0]*0.114 + original[i][j][1]*0.587 + original[i][j][2]*0.299
        # identidad
        identidad[i][j] = gris[i][j]
        # inverso
        inverso[i][j] = 255-gris[i][j]
        # umbral
        if(gris[i][j] <=35 or gris[i][j]>=100):
            umbral[i][j] = 255
        else:
            umbral[i][j] = 0
        # umbral binario
        if(gris[i][j]<35 or gris[i][j]>=100):
            Ubinario[i][j] = 255
        else:
            Ubinario[i][j] = 0
        # intervalo de umbral binario invertido
        if(gris[i][j] <35 or gris[i][j]>=100):
            UBinvertido[i][j] = 0
        else:
            UBinvertido[i][j] = 255
        # Umbral de escala de grises
        if(gris[i][j]<35 or gris[i][j]>=100):
            UescalaG[i][j] = 255
        else:
            UescalaG[i][j] = gris[i][j]
            # Umbral Escala de grises invertido
        if(gris[i][j]<35 or gris[i][j]>=100):
            UEGinvertido[i][j] = 255
        else:
            UEGinvertido[i][j] = 255 - gris[i][j]

gris = np.array(gris, dtype=np.uint8)
identidad = np.array(gris, dtype=np.uint8)
inverso = np.array(inverso, dtype=np.uint8)
umbral = np.array(umbral, dtype=np.uint8)
Ubinario = np.array(Ubinario, dtype=np.uint8)
UBinvertido = np.array(UBinvertido, dtype=np.uint8)
UescalaG = np.array(UescalaG, dtype=np.uint8)
UEGinvertido = np.array(UEGinvertido, dtype=np.uint8)

cv2.imshow('Original', gris)
cv2.imshow('Identidad', identidad)
cv2.imshow('Inverso', inverso)
cv2.imshow('Umbral', umbral)
cv2.imshow('Umbral Binario', Ubinario)
cv2.imshow('Umbral Binario Invertido', UBinvertido)
cv2.imshow('Umbral Escala de Grises', UescalaG)
cv2.imshow('Umbral Escala de Grises invertido', UEGinvertido)

histograma = cv2.calcHist([gris], [0], None, [256], [0, 256])
plt.stem(histograma)
plt.title('Histograma')
plt.xlabel('Valor de píxel')
plt.ylabel('Frecuencia')
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()

