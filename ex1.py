import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

def imagem1(m):
	width = len(m[0])
	height = len(m)
	resposta=[[0 for x in range(width)] for y in range(height)]
	for i in range(height):
		for j in range(width):
			teto = height-i
			resposta[i][j] = m[teto-1][j]
	return np.array(resposta)


img = cv.imread('img/unifafibe.jpg')
b,g,r = cv.split(img)
b1 = imagem1(b)
g1 = imagem1(g)
r1 = imagem1(r)
img2 = cv.merge((b1,g1,r1))
plt.subplot(121),plt.imshow(img, cmap="gray"),plt.title('Original')
plt.subplot(122),plt.imshow(img2, cmap="gray"),plt.title('Processed')
plt.show()

#height muda de cima para baixo e vice versa, o widght muda de esquerda para direita, e vice versa
