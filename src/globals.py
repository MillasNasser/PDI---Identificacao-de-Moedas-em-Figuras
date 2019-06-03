import numpy as np

def getColorsHSV():
    # MedianBlur size 9 + SimpleBlur 9x9
    cobre = (
        np.array([11,255,220]), # Cor mais clara do cobre
        np.array([3,100,0]))  # Cor mais escura do cobre

    # MedianBlur size 5 + SimpleBlur 5x5
    niquel = (
        np.array([179,70,200]),  # Cor mais clara do níquel
        np.array([0,0,50])) # Cor mais escura do níquel

    # MedianBlur size 9 + SimpleBlur 6x6
    bronze = (
        np.array([20, 255, 255]),  # Cor mais clara do bronze
        np.array([13, 100, 0])) # Cor mais escura do bronze

    return {
        "cobre": cobre, 
        "niquel": niquel, 
        "bronze": bronze}

def getColorsRGB():
    cobre = (
        np.array([28, 8, 4]), # Cor mais clara do cobre
        np.array([7, 0, 0]))  # Cor mais escura do cobre

    niquel = (
        np.array([61, 57, 55]),  # Cor mais clara do níquel
        np.array([10, 6, 4])) # Cor mais escura do níquel

    bronze = (
        np.array([30, 22, 11]),  # Cor mais clara do bronze
        np.array([14, 7, 0])) # Cor mais escura do bronze

    return {
        "cobre": cobre, 
        "niquel": niquel, 
        "bronze": bronze}

def getImagens(path):
    return [
        path+"circles.jpg",     # 0: Circulos coloridos
        path+"preto.png",       # 1: Todo preto
        path+"branco.png",      # 2: Todo branco
        path+"5.80.jpg",        # 3: Padrão cinza
        path+"red_5.80.jpg",    # 4: Padrão vermelho
        path+"green_5.80.jpg",  # 5: Padrão verde
        path+"blue_5.80.jpg",   # 6: Padrão azul
        path+"1cent.jpg",       # 7: Moeda 1 centavo
        path+"clean.jpg",       # 8: Cores límpidas
        path+"moedas-real.jpg", # 9: Moedas do real
    ]

def clamp(x):
    if x < 0:   return 0
    if x > 255: return 255
    return x

def hmask(threshold, img, channel):
    hist = cv2.calcHist(img,channel,None,[256],[0,256])
    return [
        1 if x>0 else 0 
        for x in [clamp(x-threshold) for x in hist]]

def apply_hmask(img):
    pass
