import numpy as np

# esse site tem as equações bem explicadas para cada feature que se deseja extrair 
# http://matlab.izmiran.ru/help/toolbox/images/graycoprops.html

def contrast(matriz):
	altura, largura = matriz.shape
	soma = 0
	for i in range(altura):
		for j in range(largura):
			soma += ((abs(i - j))**2) * matriz[i, j]

	return soma

# def correlation():


# def energy():


# def homogeneity():

