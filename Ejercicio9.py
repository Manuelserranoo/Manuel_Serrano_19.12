class Lunes:
    def __init__(self,jubilacion,nacimiento):

        self.jubilacion = jubilacion
        self.nacimiento = nacimiento
        
    def numlunes(self,jubilacion,nacimiento):
        edad = 2022 - nacimiento
        if edad<22 and edad>78:
            print("esta persona no esta en edad de trabajar") 
            pass
        elif edad>=22 and edad<=78:
            print("esta persona esta en edad de trabajar")
            

        atrabajados = jubilacion - edad
        nlun = atrabajados*48
        return nlun


if __name__ == "__main__":
    jubilacion = int(input("Ingrese su edad de jubilacion: "))
    nacimiento = int(input("Ingrese su año de nacimiento: "))
    lunes = Lunes(jubilacion,nacimiento)
    print(numlunes(jubilacion,nacimiento))
    print("Este trabajador trabajará la cantidad de :",lunes.numlunes(jubilacion,nacimiento),"lunes")
        

        
