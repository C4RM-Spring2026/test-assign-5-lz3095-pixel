import numpy as np

def getBondPrice(y, face, couponRate, m, ppy=1):
    n = int(m * ppy)
    r = y / ppy
    c = face * couponRate / ppy

    t = np.arange(1, n + 1)
    cf = np.full(n, c)
    
    cf[-1] = cf[-1] + face

    pvm = 1/ (1 + r) ** t
    pvcf=cf*pvm
    return(np.sum(pvcf))
