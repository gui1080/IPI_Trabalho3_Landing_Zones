# Aluno: Guilherme Braga Pinto
# 17/0162290

import numpy as np
import cv2

# KNN

# lemos os arquivos e dividimos 
asfalto = np.genfromtxt("asfalto.txt")
grama = np.genfromtxt("grama.txt")
perigo = np.genfromtxt("perigo.txt")
print("Arquivos de texto lidos!")
print("...")
# criamos matrizes vazias de teste e de treino
colunas, linhas = 4, 25
Matriz_asfalto_treino = [[0 for x in range(colunas)] for y in range(linhas)] 
Matriz_asfalto_teste = [[0 for x in range(colunas)] for y in range(linhas)] 

Matriz_grama_treino = [[0 for x in range(colunas)] for y in range(linhas)] 
Matriz_grama_teste = [[0 for x in range(colunas)] for y in range(linhas)] 

Matriz_perigo_treino = [[0 for x in range(colunas)] for y in range(linhas)] 
Matriz_perigo_teste = [[0 for x in range(colunas)] for y in range(linhas)] 

# divisão entre o array de asfalto
for i in range(50):
	if (i<25):
		Matriz_asfalto_treino[i][0] = asfalto[i][0]
		Matriz_asfalto_treino[i][1] = asfalto[i][1]
		Matriz_asfalto_treino[i][2] = asfalto[i][2]
		Matriz_asfalto_treino[i][3] = asfalto[i][3]
	else:
		Matriz_asfalto_teste[(i - 25)][0] = asfalto[i][0]
		Matriz_asfalto_teste[(i - 25)][1] = asfalto[i][1]
		Matriz_asfalto_teste[(i - 25)][2] = asfalto[i][2]
		Matriz_asfalto_teste[(i - 25)][3] = asfalto[i][3]

# divisão entre o array de grama
for i in range(50):
	if (i<25):
		Matriz_grama_treino[i][0] = grama[i][0]
		Matriz_grama_treino[i][1] = grama[i][1]
		Matriz_grama_treino[i][2] = grama[i][2]
		Matriz_grama_treino[i][3] = grama[i][3]
	else:
		Matriz_grama_teste[(i - 25)][0] = grama[i][0]
		Matriz_grama_teste[(i - 25)][1] = grama[i][1]
		Matriz_grama_teste[(i - 25)][2] = grama[i][2]
		Matriz_grama_teste[(i - 25)][3] = grama[i][3]

# divisão entre o array de perigo
for i in range(50):
	if (i<25):
		Matriz_perigo_treino[i][0] = perigo[i][0]
		Matriz_perigo_treino[i][1] = perigo[i][1]
		Matriz_perigo_treino[i][2] = perigo[i][2]
		Matriz_perigo_treino[i][3] = perigo[i][3]
	else:
		Matriz_perigo_teste[(i - 25)][0] = perigo[i][0]
		Matriz_perigo_teste[(i - 25)][1] = perigo[i][1]
		Matriz_perigo_teste[(i - 25)][2] = perigo[i][2]
		Matriz_perigo_teste[(i - 25)][3] = perigo[i][3]
			
	
