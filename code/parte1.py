# Aluno: Guilherme Braga Pinto
# 17/0162290

import numpy as np
import cv2
import glob
import copy
import os

from rgb_ycbcr import rgb_para_ycbcr
from features import contrast
#from features import correlation
from features import energy
from features import homogeneity
from GLCM_module import GLCM

#-----------------------------------------------------------------------------------------------------------------------------

# Este é o endereço do meu diretório de imagens quando estava trabalhando no código na minha máquina com Windows 10
# este caminho deverá ser atualizado para ser rodado em outro PC, com o caminho onde as imagens se encontram

path_asfalto="C:\\Users\\Guilherme Braga\\Desktop\\trab3\\Images\\asfalto\\*.png"
path_grama="C:\\Users\\Guilherme Braga\\Desktop\\trab3\\Images\\grama\\*.png"                                                                                                                                                                                    
path_perigo="C:\\Users\\Guilherme Braga\\Desktop\\trab3\\Images\\perigo\\*.png"

# leio todas as imagens do asfalto
array_imagens_asfalto = [cv2.imread(file) for file in glob.glob(path_asfalto)]
numero_imagens_asfalto = len(array_imagens_asfalto)
altura_asfalto, largura_asfalto, channels_asfalto = array_imagens_asfalto[0].shape

# apenas para checar as imagens lidas
print("Imagens do asfalto lidas: ")
print(numero_imagens_asfalto)

# leio todas as imagens da grama
array_imagens_grama = [cv2.imread(file) for file in glob.glob(path_grama)]
numero_imagens_grama = len(array_imagens_grama)
altura_grama, largura_grama, channels_grama = array_imagens_grama[0].shape

# apenas para checar as imagens lidas
print("Imagens da grama lidas: ")
print(numero_imagens_grama)

# leio todas as imagens de perigo
array_imagens_perigo = [cv2.imread(file) for file in glob.glob(path_perigo)]
numero_imagens_perigo = len(array_imagens_perigo)
altura_perigo, largura_perigo, channels_perigo = array_imagens_perigo[0].shape

# apenas para checar as imagens lidas
print("Imagens de perigo lidas: ")
print(numero_imagens_perigo)

# no total, lemos as 150 imagens disponibilizadas

#-----------------------------------------------------------------------------------------------------------------------------

# para facilitar, pretende-se aplicar o KNN em outro módulo, o atual módulo salvará as caracteristicas das imagens em um arquivo externo
# >contrast
# >correlation 
# >energy
# >homogeneity 
# (tudo retirado a partir da GLCM)

# faremos uma matriz das 4 caracteristas, posição 0 = contrast, posição 1 = correlation, posição 2 = energy, posição 3 = homogeneity 
colunas, linhas = 4, 50
Matriz_caracteristicas_asfalto = [[0 for x in range(colunas)] for y in range(linhas)] 

#-----------------------------------------------------------------------------------------------------------------------------

# ASFALTO

# primeiras 25 imagens são treino, as outras são teste
print("Imagens do asfalto sendo processadas...")
for i in range(numero_imagens_asfalto):
    imagem = rgb_para_ycbcr(array_imagens_asfalto[i]) 

    matrizGLCM = GLCM(imagem, altura_asfalto, largura_asfalto) 
    matrizGLCM /= np.sum(matrizGLCM)

    Matriz_caracteristicas_asfalto[i][0] = contrast(matrizGLCM)
    #printf("Contraste processado!")
    #Matriz_caracteristicas_asfalto[i][1] = correlation(matrizGLCM)
    #printf("Correlação processada!")
    Matriz_caracteristicas_asfalto[i][2] = energy(matrizGLCM)
    #printf("Energia processada!")
    Matriz_caracteristicas_asfalto[i][3] = homogeneity(matrizGLCM)
    #printf("Homogeneidade processada!")

    print("A seguinte imagem do array de imagens do asfalto acaba de ser processada!")
    print(i + 1)

#-----------------------------------------------------------------------------------------------------------------------------

# GRAMA



#-----------------------------------------------------------------------------------------------------------------------------

# PERIGO



#-----------------------------------------------------------------------------------------------------------------------------
