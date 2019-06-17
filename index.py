import cv2
import sys
import numpy as np
import src.globals as g_coin
import src.filters as filtro
import matplotlib.pyplot as plt

def getMoedas(rgb_img, v):
    moedas = []
    mascara = filtro.f_moedas(v)
    saida = cv2.connectedComponentsWithStats(mascara)
    for i in range(1,saida[0]):
        info = saida[2][i]
        lbl = saida[1].copy()
        lbl[lbl != i] = 0; lbl[lbl == i] = 255

        lbl = np.array(lbl,np.uint8)
        appl_mask = cv2.bitwise_and(rgb_img,rgb_img,mask=lbl)

        x1 = info[1]; y1 = info[0]
        x2 = x1+info[2]; y2 = y1 + info[3]
        moeda = appl_mask[x1:x2, y1:y2]

        #! Mudar depois para algo mais inteligente
        #? Obs: Pode ser resolvido com proporção?
        if(info[4] > 100): moedas.append((moeda, info[4]))
    return moedas

# Definições globais
# -------------------------------------------------------- #
# 0: Circulos coloridos # 1: Todo preto
# 2: Todo branco        # 3: Padrão cinza
# 4: Padrão vermelho    # 5: Padrão verde
# 6: Padrão azul        # 7: Moeda 1 centavo
# 8: Cores límpidas     # 9: Moedas do real
path = './testes/'
testes = g_coin.getImagens(path)
bgr_img = cv2.imread(testes[int(sys.argv[1])])

# Coloração base em RGB (dict keys: cobre, niquel, bronze)
color_rgb = g_coin.getColorsRGB()
color_hsv = g_coin.getColorsHSV()

# Definião da imagem a ser analisada
# -------------------------------------------------------- #
rgb_img = cv2.cvtColor(bgr_img, cv2.COLOR_BGR2RGB)
hsv_img = cv2.cvtColor(bgr_img, cv2.COLOR_BGR2HSV)

width, height, _ = hsv_img.shape
r, g, b = cv2.split(rgb_img)
h, s, v = cv2.split(hsv_img)

# Algoritmos
# -------------------------------------------------------- #
moedas = getMoedas(rgb_img, v)

# Exibição dos Resultados
# -------------------------------------------------------- #
#! Grid funcional apenas para as imagens 3,4,5,6 e 9!!
plt.figure()
for i in range(0,3):
    for j in range(0,4):
        plt.subplot(3,4,i*4+j +1)
        plt.yticks([]); plt.xticks([]) 
        plt.imshow(moedas[i*4+j][0])

plt.figure()
plt.xticks([]); plt.yticks([])
plt.imshow(rgb_img, cmap=plt.get_cmap("gray"))

plt.show()