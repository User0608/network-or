import network

if __name__ == "__main__":
    network.learn()
    prueba = [[1, 1], [1, 0], [0, 0], [1, 1], [1, 1], [1, 0], [0, 0], [1, 1]]
    for p in prueba:
        network.pronosticar(p)
