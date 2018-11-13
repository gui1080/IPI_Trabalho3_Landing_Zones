# Aluno: Guilherme Braga Pinto
# 17/0162290

import numpy as np

def euclidian_distance(coordenada_asfalto, coordenada_perigo, coordenada_grama, coordenada_atual, i):

	dist_asf = ( (  ((abs(coordenada_atual[i][0] - coordenada_asfalto[0]))**2) + ((abs(coordenada_atual[i][1] - coordenada_asfalto[1]))**2) + ((abs(coordenada_atual[i][2] - coordenada_asfalto[2]))**2) ) **(1/2))

	dist_per = ( (  ((abs(coordenada_atual[i][0] - coordenada_perigo[0]))**2) + ((abs(coordenada_atual[i][1] - coordenada_perigo[1]))**2) + ((abs(coordenada_atual[i][2] - coordenada_perigo[2]))**2)  ) **(1/2))

	dist_gra = ( (  ((abs(coordenada_atual[i][0] - coordenada_grama[0]))**2) + ((abs(coordenada_atual[i][1] - coordenada_grama[1]))**2) + ((abs(coordenada_atual[i][2] - coordenada_grama[2]))**2)  ) **(1/2))

	if(dist_asf < dist_per): 
		if(dist_asf < dist_gra):
			return 1
	if(dist_gra < dist_per): 
		if(dist_gra < dist_asf):
			return 2
	if(dist_per < dist_gra): 
		if(dist_per < dist_asf):
			return 3



#def vizinhos():
