import cv2
import numpy as np
import matplotlib.pyplot as plt

# Carregue suas imagens aqui
imagem1 = cv2.imread('enhance-me.tiff', cv2.IMREAD_COLOR)
imagem2 = cv2.imread('fractured.tif', cv2.IMREAD_COLOR)


valores_gamma = [0.5, 1.0, 1.5, 2.0]

for gamma in valores_gamma:
    # Aplicar a transformação de potência
    imagem1_transformada = np.power(imagem1, gamma)
    imagem2_transformada = np.power(imagem2, gamma)

    # Normalizar os valores dos pixels para o intervalo [0, 255]
    imagem1_transformada = cv2.normalize(imagem1_transformada, None, 0, 255, cv2.NORM_MINMAX, dtype=cv2.CV_8U)
    imagem2_transformada = cv2.normalize(imagem2_transformada, None, 0, 255, cv2.NORM_MINMAX, dtype=cv2.CV_8U)

    # Mostrar as imagens transformadas
    plt.figure(figsize=(12, 6))
    plt.subplot(1, 2, 1)
    plt.imshow(cv2.cvtColor(imagem1_transformada, cv2.COLOR_BGR2RGB))
    plt.title(f'Imagem 1 - Gamma={gamma}')
    plt.subplot(1, 2, 2)
    plt.imshow(cv2.cvtColor(imagem2_transformada, cv2.COLOR_BGR2RGB))
    plt.title(f'Imagem 2 - Gamma={gamma}')
    plt.show()
