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
        try:
            index = pmask.index(pxl)
            cmask.append(pmask.pop(index))

            x = pxl[0]; y = pxl[1]
            for i in range(-1,2):
                for j in range(-1,2):
                    clustering((x+i,y+j), pmask, cmask)
        except: pass

    clusters = []
    pixels = fmask_positivo(mask,factor)
    while pixels != []:
        cmask = []
        clustering(pixels[0], pixels, cmask)
        clusters.append(cmask)
    return clusters
