
def tribonacci():

    a = 0

    b = 0

    c = 1

    for i in range(0, 10):

        print(a)

        a = b

        b = c

        c = a + b + c
    return c


if __name__ == "__main__":

    tribonacci()
