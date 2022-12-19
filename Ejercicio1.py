def resolver_nonograma(filas,columnas,pistf,pistc):
    matriz = [[0 for k in range(columnas)] for k in range(filas)]

    for i in range(filas):
        usar_pistas(matriz,i,pistc[i])
        return matriz
    for j in range (columnas):
        usar_pistas(matriz,j,pistf[j])
        return matriz
def usar_pistas(matriz,index,pistas,a = True):
    i = 0
    for p in pistas:
        for k in range(p):
            if a :
                matriz[index][i] = 1
            else:
                matriz[i][index] = 1
            i = i + 1
        i = i + 1
    

    





if __name__ == "__main__":
    filas = 5
    columnas = 5
    pistc = [[1],[1,1],[1,1,1],[3],[1]]
    pistf = [[1],[2],[3],[2,1],[4]]
    print(resolver_nonograma(filas,columnas,pistf,pistc))