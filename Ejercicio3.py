class Numeros:
    def __init__(self, numeros):
        self.numero = numeros
        self.letra = ""
        self.lnumeros = [10,9,8,7,6,5,4,3,2,1]
        self.letras = ["ten","nine","eight","seven","six","five","four","three","two","one"]
    def convertirnumeros(self):
        for i in range(len(self.valores)):
            while self.numero >= self.lnumeros[i]:
                self.numero -= self.lnumeros[i]
                self.letra += self.letras[i]
        return self.letra
        


if __name__ == "__main__":
    numero = int(input("Ingrese un numero: "))
    letra = Numeros(numero)
    print(letra.convertirnumeros())