def resolver_nonograma(filas,columnas,pistf,pistc)
    matriz = [[0 for i in range(columnas)] for j in range(filas)]

    for i in range(filas):
        usar_pistas(matriz,j,pistc[j])
        return matriz

def usar_pistas(matriz,fila,pista):
    for i in range(len(pista)):
        for j in range(pista[i]):
            matriz[fila][j] = 1
        matriz[fila][j] = 2
    return matriz






if __name__ == "__main__":
    filas = 5
    columnas = 5
    pistc = [[1],[1,1],[1,1,1],[3],[1]]
    pistc = [[1],[2],[3],[2,1],[4]]
    print(resolver_nonograma(filas,columnas,pistf,pistc))