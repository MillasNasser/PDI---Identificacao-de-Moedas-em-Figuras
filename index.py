import cv2
import numpy as np
import src.globals as g_coin
import src.filters as filtro
import matplotlib.pyplot as plt

# Definições globais
# -------------------------------------------------------- #
# 0: Circulos coloridos # 1: Todo preto
# 2: Todo branco        # 3: Padrão cinza
# 4: Padrão vermelho    # 5: Padrão verde
# 6: Padrão azul        # 7: Moeda 1 centavo
# 8: Cores límpidas     # 9: Moedas do real
path = './testes/'
testes = g_coin.getImagens(path)
bgr_img = cv2.imread(testes[5])

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
hsv_img = cv2.blur(hsv_img, (2,2))

lb = np.array(color_hsv['bronze'][1])
ub = np.array(color_hsv['bronze'][0])
mascara = cv2.inRange(hsv_img, lb, ub)

# Plotando as figuras
# -------------------------------------------------------- #
lb = np.array(color_hsv['cobre'][1])
ub = np.array(color_hsv['cobre'][0])
mascara = cv2.inRange(hsv_img, lb, ub)
# -------------------------------------------------------- #
plt.subplot("311"); plt.xticks([]), plt.yticks([])  
median_blur = cv2.medianBlur(mascara, 9)
simple_blur = cv2.blur(median_blur, (6,6))
result = cv2.bitwise_and(rgb_img, rgb_img, mask=simple_blur)
plt.imshow(result, cmap=plt.get_cmap("gray"))


lb = np.array(color_hsv['niquel'][1])
ub = np.array(color_hsv['niquel'][0])
mascara = cv2.inRange(hsv_img, lb, ub)
# -------------------------------------------------------- #
plt.subplot("312"); plt.xticks([]), plt.yticks([])  
median_blur = cv2.medianBlur(mascara, 9)
simple_blur = cv2.blur(median_blur, (6,6))
result = cv2.bitwise_and(rgb_img, rgb_img, mask=simple_blur)
plt.imshow(result, cmap=plt.get_cmap("gray"))


lb = np.array(color_hsv['bronze'][1])
ub = np.array(color_hsv['bronze'][0])
mascara = cv2.inRange(hsv_img, lb, ub)
# -------------------------------------------------------- #
plt.subplot("313"); plt.xticks([]), plt.yticks([])  
median_blur = cv2.medianBlur(mascara, 9)
simple_blur = cv2.blur(median_blur, (6,6))
result = cv2.bitwise_and(rgb_img, rgb_img, mask=simple_blur)
plt.imshow(result, cmap=plt.get_cmap("gray"))

a = filtro.fmask_positivo(mascara,200)
print(len(filtro.fmask_cluster(mascara)))

plt.show()