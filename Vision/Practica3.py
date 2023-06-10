# ***************************************************
# ARCHIVO: Practica3.py
#
# DESCRIPCIÓN: 
# Transformación entre modelos de color
# CMY, CMYK, HSI, HSV, YCbCR y Escala de grises
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
[fila,columna,pixel] = original.shape

# Creación de matrices vacías
cmy = np.zeros((fila,columna,pixel))
CMYK = np.zeros((fila,columna,4))
hsi = np.zeros((fila,columna,pixel))
hsv  = np.zeros((fila,columna,pixel))
YCbCr = np.zeros((fila,columna,pixel))
EscalaGrises = np.zeros((fila,columna))


for i in range(fila):
    for j in range(columna):
        # *******************************************************
        # conversion a CMY
        # *******************************************************
        r, g, b = original[i, j]
        c = 255 - r
        m = 255 - g
        y = 255 - b
        cmy[i, j, 0] = c
        cmy[i, j, 1] = m
        cmy[i, j, 2] = y

        # *******************************************************
        # Conversion a CMYK
        # *******************************************************
        k = min(c, m, y)
        # Calcular los valores de C, M y Y en función de K
        if k != 255:
            CMYK[i, j, 0] = (c - k) * 255 // (255 - k)
            CMYK[i, j, 1] = (m - k) * 255 // (255 - k)
            CMYK[i, j, 2] = (y - k) * 255 // (255 - k)

        # Asignar el valor de K
        CMYK[i, j, 3] = k

        # *******************************************************
        # Conversion a HSI
        # *******************************************************
        # Convertir los valores RGB a valores normalizados en el rango [0, 1]
        r_norm = r / 255
        g_norm = g / 255
        b_norm = b / 255

        # Calcular el valor de Intensity (I)
        i_val = (r_norm + g_norm + b_norm) / 3

        # Calcular el valor de Saturation (S)
        min_val = min(r_norm, g_norm, b_norm)
        s_val = 1.0 - (3.0 * min_val / (r_norm + g_norm + b_norm)) if (r_norm + g_norm + b_norm) != 0 else 0

        # Calcular el valor de Hue (H)
        if s_val != 0:
            num = 0.5 * ((r_norm - g_norm) + (r_norm - b_norm))
            den = ((r_norm - g_norm) ** 2 + (r_norm - b_norm) * (g_norm - b_norm)) ** 0.5
            theta = np.arccos(num / den) if den != 0 else 0

            if b_norm <= g_norm:
                h_val = theta
            else:
                h_val = 2 * np.pi - theta

            h_val /= 2 * np.pi
        else:
            h_val = 0

        # Asignar los valores de H, S y I a la matriz HSI
        hsi[i, j, 0] = h_val
        hsi[i, j, 1] = s_val
        hsi[i, j, 2] = i_val

        # *******************************************************
        # Conversion a HSV
        # *******************************************************
        c_max = max(r_norm, g_norm, b_norm)
        c_min = min(r_norm, g_norm, b_norm)
        delta = c_max - c_min

        # Calcular el valor de Hue (H)
        if delta == 0:
            hue_val = 0
        elif c_max == r_norm:
            hue_val = (60 * ((g_norm - b_norm) / delta) + 360) % 360
        elif c_max == g_norm:
            hue_val = (60 * ((b_norm - r_norm) / delta) + 120) % 360
        else:
            hue_val = (60 * ((r_norm - g_norm) / delta) + 240) % 360

        # Calcular el valor de Saturation (S)
        if c_max == 0:
            saturation_val = 0
        else:
            saturation_val = delta / c_max

        # Calcular el valor de Value (V)
        value = c_max

        # Asignar los valores de H, S y V a la matriz HSV
        hsv[i, j, 0] = int(hue_val * 255 / 360)
        hsv[i, j, 1] = int(saturation_val * 255)
        hsv[i, j, 2] = int(value * 255)

        # *******************************************************
        # Conversion a YCbCr
        # *******************************************************
        y_val = int(0.299 * r + 0.587 * g + 0.114 * b)
        cb_val = int(128 - 0.169 * r - 0.331 * g + 0.5 * b)
        cr_val = int(128 + 0.5 * r - 0.419 * g - 0.081 * b)
        # Asignar los valores de Y, Cb y Cr a la matriz YCbCr
        YCbCr[i, j, 0] = y_val
        YCbCr[i, j, 1] = cb_val
        YCbCr[i, j, 2] = cr_val

        # *******************************************************
        # Conversion a escala de grises
        # *******************************************************
        EscalaGrises[i][j] = original[i][j][0]*0.114 + original[i][j][1]*0.587 + original[i][j][2]*0.299
      


# Conversion de matrices a uint8 
original = np.array(original, dtype=np.uint8)
cmy = np.array(cmy, dtype=np.uint8)
CMYK = np.array(CMYK, dtype=np.uint8)
hsi *= 255
hsi = np.array(hsi, dtype=np.uint8)
hsv = np.array(hsv, dtype=np.uint8)
YCbCr = np.array(YCbCr, dtype=np.uint8)
EscalaGrises = np.array(EscalaGrises, dtype=np.uint8)

# Mostrar imágenes
cv2.imshow('Original', original)
cv2.imshow('CMY', cmy)
cv2.imshow('CMYK', CMYK)
cv2.imshow('HSI', hsi)
cv2.imshow('HSV', hsv)
cv2.imshow('YCbCr', YCbCr)
cv2.imshow('Escala de Grises', EscalaGrises)
cv2.waitKey(0)
cv2.destroyAllWindows()