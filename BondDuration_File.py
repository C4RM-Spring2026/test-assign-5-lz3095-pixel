import numpy as np

def getBondDuration(y, face, couponRate, m, ppy = 1):
    n = int(m * ppy)
    r = y / ppy
    c = face * couponRate / ppy

    t = np.arange(1, n + 1)
    cf = np.full(n, c)
    cf[-1] = cf[-1] + face

    pvm = 1 / (1 + r) ** t
    pvcf=pvm*cf
    bondPrice = np.sum(pvcf)

    bondDuration=np.sum(t*pvcf)/bondPrice/ppy
    
    return(bondDuration)
