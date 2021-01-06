import data
xor = {"00": 0, "01": 1, "10": 1, "11": 1, }
XX = [[0, 0], [0, 1], [1, 0], [1, 1]]


def loadData():
    pesos = data.getWeights()
    if len(pesos) == 0:
        arr = []
        arr.append(data.randomWeight())
        arr.append(data.randomWeight())
        arr.append(data.randomWeight())
        data.setWeights(arr)
        pesos = data.getWeights()
    return pesos


def calculoFuncion(X=[0, 0, 0]):
    result = 0.0
    pesos = loadData()
    i = 0
    for p in pesos:
        result += p*X[i]
        i += 1
    return result


def evaluar(X1, X2):
    pesos = data.getWeights()
    X = [X1, X2, 1]
    net = calculoFuncion(X)
    key = str(X1)+str(X2)

    Yo = data.funcionEscalon(net)
    Yd = xor[key]
    if Yo != Yd:
        newPesos = []
        i = 0
        for w in pesos:
            newPesos.append(data.reglaDeltaGeneralizada(
                w=w, yd=Yd, y0=Yo, xi=X[i]))
            i += 1
        data.setWeights(newPesos)
        print("learning...")
        return False
    print("...")
    return True


def learn():
    trues = 0
    while(True):
        for x in XX:
            if evaluar(x[0], x[1]):
                trues += 1
        if len(xor) == trues:
            break
        else:
            trues = 0
    print("Complete...")


def pronosticar(xx=[]):
    X = [xx[0], xx[1], 1]
    Yo = data.funcionEscalon(calculoFuncion(X))
    print(X[0], " or ", X[1], " = ", Yo)


if __name__ == "__main__":
    prueba = [[1, 1], [1, 0], [0, 0], [1, 1], [1, 1], [1, 0], [0, 0], [1, 1]]
    for p in prueba:
        pronosticar(p)
