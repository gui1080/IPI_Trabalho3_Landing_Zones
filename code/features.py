import numpy as np

# esse site tem as equações bem explicadas para cada feature que se deseja extrair 
# http://matlab.izmiran.ru/help/toolbox/images/graycoprops.html

def contrast(matriz):
	altura, largura = matriz.shape
	soma = 0
	for x in range(altura):
		for y in range(largura):
			soma += (((abs(x - y))**2) * matriz[x, y])
			# abs = absolute value

	return soma

def correlation(matriz):
    height, width = matriz.shape
    listSumI = []
    listSumJ = []

    for i, j in zip(range(height), range(width)):
        sumI = np.sum(matriz[i, :])
        sumJ = np.sum(matriz[:, j])
        listSumI.append(sumI)
        listSumJ.append(sumJ)
        sumI = 0
        sumJ = 0

    mediaI = 0
    mediaJ = 0

    for i in range(1, height+1):
        mediaI += i * (listSumI[i-1])
    for j in range(1, width+1):
        mediaJ += j * (listSumJ[j-1])

    variancia_aux_I = 0
    for i in range(1, height+1):
        variancia_aux_I += ((i - mediaI)**2) * listSumI[i - 1]
    desvio_padraoI = variancia_aux_I**(1/2)
    
    variancia_aux_J = 0
    for j in range(1, width+1):
        variancia_aux_J += ((j - mediaJ)**2) * listSumJ[j - 1]
    desvio_padraoJ = variancia_aux_J**(1/2)

    soma = 0
    for i in range(1, height+1):
        for j in range(1, width+1):
            soma += (((i - mediaI) * (j - mediaJ) * matriz[i-1, j-1])/(desvio_padraoI * desvio_padraoJ))
    return soma


def energy(matriz):
	altura, largura = matriz.shape
	soma = 0
	
	for x in range(altura):	
		for y in range(largura):
			soma += ((matriz[x, y])**2)
	return soma


def homogeneity(matriz):
	altura, largura = matriz.shape
	soma = 0
	
	for x in range(altura):	
		for y in range(largura):
			soma += ((matriz[x, y])/(1 + (abs(x - y))))
			# abs = absolute value
			
	return soma


