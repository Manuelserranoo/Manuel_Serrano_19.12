def domath():
    palabra = "24z6 1x23 y369 89a 900b"
    lista = []
    for i in palabra:
        if i == "z":
            palabra.replace("z","j")
        elif i == "x":
            palabra.replace("x","j")
        elif i == "y":
            palabra.replace("y","j")
        elif i == "a":
            palabra.replace("a","j")
        elif i == "b":
            palabra.replace("b","j")

    return palabra




if __name__ == "__main__":
    print(domath())