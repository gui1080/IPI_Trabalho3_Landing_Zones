# Aluno: Guilherme Braga Pinto
# 17/0162290

import numpy as np
import cv2
from euclidian_distance import euclidian_distance 
#from euclidian_distance import vizinhos

# KNN - K´s Nearest Neighbour

#----------------------------------------------------------LEITURA DOS ARQUIVOS-------------------------------------------------------------------

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

#---------------------------------------------------DIVISAO ENTRE IMAGEM DE TESTE E DE TREINO--------------------------------------------------------------------------

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

#-----------------------------------------------------PONTO MEDIO DE CADA TIPO DE IMAGEM------------------------------------------------------------------------

media_asfalto = []
media_0 = 0
media_1 = 0
media_2 = 0
media_3 = 0


for i in range(25):
	media_0 += Matriz_asfalto_treino[i][0] 
	media_1 += Matriz_asfalto_treino[i][1]
	media_2 += Matriz_asfalto_treino[i][2]
	media_3 += Matriz_asfalto_treino[i][3]

media_asfalto.insert(0, (media_0/25))
media_asfalto.insert(1, (media_1/25))
media_asfalto.insert(2, (media_2/25))
media_asfalto.insert(3, (media_3/25))


media_grama = []
media_0 = 0
media_1 = 0
media_2 = 0
media_3 = 0


for i in range(25):
	media_0 += Matriz_grama_treino[i][0] 
	media_1 += Matriz_grama_treino[i][1]
	media_2 += Matriz_grama_treino[i][2]
	media_3 += Matriz_grama_treino[i][3]

media_grama.insert(0, (media_0/25))
media_grama.insert(1, (media_1/25))
media_grama.insert(2, (media_2/25))
media_grama.insert(3, (media_3/25))


media_perigo = []
media_0 = 0
media_1 = 0
media_2 = 0
media_3 = 0


for i in range(25):
	media_0 += Matriz_perigo_treino[i][0] 
	media_1 += Matriz_perigo_treino[i][1]
	media_2 += Matriz_perigo_treino[i][2]
	media_3 += Matriz_perigo_treino[i][3]

media_perigo.insert(0, (media_0/25))
media_perigo.insert(1, (media_1/25))
media_perigo.insert(2, (media_2/25))
media_perigo.insert(3, (media_3/25))

print("Médias do set de treino calculadas!")
print("...")

#--------------------------------------------------TESTES---------------------------------------------------------------------------

print("Executando testes das imagens do asfalto!")
print("...")

nao_pousar = 0
pousar = 0

asfalto_afirmativo = 0
asfalto_negativo = 0

for i in range(25):
	teste = euclidian_distance(media_asfalto, media_perigo, media_grama, Matriz_asfalto_teste, i)

	if(teste == 1):
		asfalto_afirmativo += 1
	else:
		asfalto_negativo += 1

	if(teste == 3):
		nao_pousar += 1
	else:
		pousar += 1

acerto_geral_asfalto = ((asfalto_afirmativo * 100) /25)

print("Quantidade de imagens do asfalto que foram reconhecidas como asfalto:")
print(asfalto_afirmativo)

print("Porcentagem de acertos das imagens de asfalto:")
print(acerto_geral_asfalto)

print("Executando testes das imagens da grama!")
print("...")

grama_afirmativo = 0
grama_negativo = 0

for i in range(25):
	teste = euclidian_distance(media_asfalto, media_perigo, media_grama, Matriz_grama_teste, i)

	if(teste == 2):
		grama_afirmativo += 1
	else:
		grama_negativo += 1

	if(teste == 3):
		nao_pousar += 1
	else:
		pousar += 1

acerto_geral_grama = ((grama_afirmativo * 100) /25)

print("Quantidade de imagens da grama que foram foram reconhecidas como grama:")
print(grama_afirmativo)

print("Porcentagem de acertos das imagens de grama")
print(acerto_geral_grama)

print("Executando testes das imagens de perigo!")
print("...")

perigo_afirmativo = 0
perigo_negativo = 0

for i in range(25):
	teste = euclidian_distance(media_asfalto, media_perigo, media_grama, Matriz_perigo_teste, i)

	if(teste == 3):
		perigo_afirmativo += 1
	else:
		perigo_negativo += 1

	if(teste == 3):
		nao_pousar += 1
	else:
		pousar += 1

acerto_geral_perigo = ((perigo_afirmativo * 100) /25)

acerto_medio = ((acerto_geral_perigo + acerto_geral_grama + acerto_geral_asfalto) / 3)

print("Quantidade de imagens de perigo que foram foram reconhecidas como perigo:")
print(perigo_afirmativo)

print("Porcentagem de acertos das imagens de perigo")
print(acerto_geral_perigo)

print("De 75 imagens de test, esta foi a quantidade de imagens consideradas como perigosas para pouso:")
print(nao_pousar)

print("De 75 imagens de test, esta foi a quantidade de imagens consideradas como seguras para pouso:")
print(pousar)

print("Porcentagem media dos acertos:")
print(acerto_medio)

#-----------------------------------------------------------------------------------------------------------------------------
