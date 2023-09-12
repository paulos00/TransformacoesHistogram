import cv2
import numpy as np

# Função para aplicar a transformação logarítmica
def apply_log_transformation(image, c):
    log_transformed = c * np.log1p(image)
    return np.uint8(log_transformed)

# Carregue as duas imagens
image1 = cv2.imread('fractured.tif')
image2 = cv2.imread('enhance-me.tiff')

# Defina o valor do parâmetro c (ajuste para obter o resultado desejado)
c = 100

# Aplique a transformação logarítmica às duas imagens
transformed_image1 = apply_log_transformation(image1, c)
transformed_image2 = apply_log_transformation(image2, c)

# Exiba as imagens originais e transformadas
cv2.imshow('Imagem 1 Original', image1)
cv2.imshow('Imagem 1 Transformada', transformed_image1)
cv2.imshow('Imagem 2 Original', image2)
cv2.imshow('Imagem 2 Transformada', transformed_image2)

# Aguarde até que uma tecla seja pressionada e feche as janelas
cv2.waitKey(0)
cv2.destroyAllWindows()
