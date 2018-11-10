# Aluno: Guilherme Braga Pinto
# 17/0162290

import numpy as np

def rgb_para_ycbcr(imagem):


# img[i, j, 0]  #pixel da matriz azul
# img[i, j, 1]  #pixel da matriz verde
# img[i, j, 2]) #pixel da matriz vermelha

    height, width, channels = imagem.shape

# crio matrizes vazias
    imagemY = np.zeros((height, width), dtype=np.int8)
    #imagemCr = np.zeros((height, width), dtype=np.int8)
    #imagemCb = np.zeros((height, width), dtype=np.int8)

# preencho usando o que foi estabelecido
    imagemY[:, :] = (0.114 * imagem[:, :, 0] + 0.587 * imagem[:, :, 1] + 0.299 * imagem[:, :, 2])
    #imagemCr = (0.713 * imagem[:, :, 2] - 0.713 * imagemY + 128)
    #imagemCb = (0.564 * imagem[:, :, 0] - 0.564 * imagemY + 128)
    return imagemY