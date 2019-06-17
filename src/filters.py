import cv2
import numpy as np

def fmask_positivo(mask, factor=230):
    width, height = mask.shape
    result = []
    for i in range(0,width):
        for j in range(0, height):
            if mask[i][j] > factor:
                result.append((i,j))
    return result


def fmask_cluster(mask, factor=230):
    def clustering(pxl, pmask, cmask):
        stack = [pxl]
        while stack != []:
            pxl = stack.pop()
            try: index = pmask.index(pxl)
            except: continue

            cmask.append(pmask.pop(index))

            x = pxl[0]; y = pxl[1]
            for i in range(-1,2):
                for j in range(-1,2):
                    stack.append((x+i,y+j))

    clusters = []
    pixels = fmask_positivo(mask,factor)
    while pixels != []:
        cmask = []
        clustering(pixels[0], pixels, cmask)
        clusters.append(cmask)
    return clusters

def f_moedas(img):
    kernel = np.array([[1,1,1],[1,-8,1],[1,1,1]])
    laplacian = cv2.filter2D(img, -1, kernel)
    laplacian = cv2.threshold(laplacian, 30, 255, cv2.THRESH_BINARY)[1]

    kernel = np.ones((1,1), np.uint8)
    laplacian = cv2.morphologyEx(laplacian, cv2.MORPH_OPEN, kernel)

    des = laplacian

    for _ in range(0, 5):
        contour = cv2.findContours(des,cv2.RETR_CCOMP,cv2.CHAIN_APPROX_SIMPLE)[0]
        for cnt in contour:
            abigail = cv2.convexHull(cnt, False)
            cv2.drawContours(des,[abigail],0,255,-1)

    kernel = np.ones((9,9), np.uint8)
    laplacian = cv2.morphologyEx(laplacian, cv2.MORPH_OPEN, kernel)
    return laplacian