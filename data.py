import random


def randomWeight():
    return random.uniform(-3, 3)


def getWeights():
    f = open("base.data", "r")
    pesos = []
    while(True):
        linea = f.readline()
        if not linea:
            break
        pesos.append(float(linea.replace("\n", "")))
    f.close()
    return pesos


def setWeights(weights=[]):
    f = open("base.data", 'w')
    for w in weights:
        f.write(str(w) + '\n')
    f.close()


def funcionEscalon(net):
    if net >= 0:
        return 1
    if net < 0:
        return 0


def reglaDeltaGeneralizada(w, yd, y0, xi, f=0.5):
    return w+f*(yd-y0)*xi
