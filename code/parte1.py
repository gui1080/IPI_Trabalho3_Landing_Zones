# Aluno: Guilherme Braga Pinto
# 17/0162290

import numpy as np
import cv2
import glob
import copy
import os

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

#-----------------------------------------------------------------------------------------------------------------------------
