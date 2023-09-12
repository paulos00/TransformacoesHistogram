import cv2
import matplotlib.pyplot as plt

# Carregar a imagem usando o OpenCV
imagem = cv2.imread('enhance-me.tiff', cv2.IMREAD_GRAYSCALE)

# Realizar a equalização de histograma
imagem_equalizada = cv2.equalizeHist(imagem)


# Plotar a imagem original
plt.subplot(1, 2, 1)
plt.title('Imagem Original')
plt.imshow(imagem, cmap='gray')

# Plotar a imagem equalizada
plt.subplot(1, 2, 2)
plt.title('Imagem Equalizada')
plt.imshow(imagem_equalizada, cmap='gray')

# Exibir as imagens
plt.tight_layout()
plt.show()
