import numpy as np
import cv2

# !!!Gray-Level Co-Occurrence Matrix!!!

def GLCM (imagem, altura, largura):
	
	listHistogram = []

	# no caso, Histogram_imagem e GLCM funcionam como um dicionario para fazer a operação nos if´s dentro dos for funcionarem
	# não necessáriamente atrelaremos um nome a cada posição, apenas faremos um tipo de index
	Histogram_imagem = {}
	GLCM = {}
	pixel_atual = (0, 1)
	for x in range(altura):
		for y in range(largura - 1):
			# fazendo até a largura normal não foi possível, pois em algum ponto imagem[x, y +1] não existirá 

			# x_atual = [x, y]
			# y_atual = [x, y + 1]
			
			pixel_atual = (imagem[x, y], imagem[x, y + 1]) 
			
			# se a posição que queremos não é zero, então adicionamos 1, se é zero, faremos com que seja 1 para iniciar
			if pixel_atual in GLCM: 
				GLCM[pixel_atual] += 1
			else:
				GLCM[pixel_atual] = 1

	for i in range(altura):
		for j in range(largura):
			if imagem[i, j] in Histogram_imagem:
				Histogram_imagem[imagem[i, j]] += 1
			else:
				Histogram_imagem[imagem[i, j]] = 1
				listHistogram.insert(0, imagem[i, j])

	listHistogram.sort()
	tam_histogram = len(Histogram_imagem)
	# fazemos uma matriz vazia para uma matriz de GLCM, efetivamente
	matrizGLCM = np.zeros((tam_histogram, tam_histogram), dtype=np.float32)
	
	for n, i in zip(listHistogram, range(tam_histogram)):
		for m, j in zip(listHistogram, range(tam_histogram)):
			if (n, m) in GLCM:
				matrizGLCM[i, j] = GLCM[(n, m)]
	return matrizGLCM	