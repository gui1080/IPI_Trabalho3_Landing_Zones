import numpy as np

# esse site tem as equações bem explicadas para cada feature que se deseja extrair 
# http://matlab.izmiran.ru/help/toolbox/images/graycoprops.html

def contrast(matriz):
	altura, largura = matriz.shape
	soma = 0
	for x in range(altura):
		for y in range(largura):
			soma += ((abs(x - y))**2) * matriz[x, y]

	return soma

# def correlation():


def energy(matriz):
	altura, largura = matriz.shape
	soma = 0
	
	for x in range(altura):	
		for y in range(largura):
			soma += (matriz[x, y])**2
	return soma


# def homogeneity():

