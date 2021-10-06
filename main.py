import random
def humanguess():
    number = random.randrange(0,10)
    print (number)
    numero=0

    while numero!=number:
        numero=int(input("INTRODUCE UN NUMERO "))
        if number==numero:
            print(f"FELICIDADES GANASTE EL NUMERO ERA {number}")
        elif numero>number:
            print(f"EL NUMERO QUE ELIGIO ES MAYOR A {number}")
        else:
            print(f"EL NUMERO QUE ELIGIO ES MENOR A {number}")

humanguess()