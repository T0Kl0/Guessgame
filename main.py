import random
def humanguess():
    number = random.randrange(0,10)
    print (number)
    numero=1

    while numero!=number:
        numero=int(input("INTRODUCE UN NUMERO "))
        if number==numero:
            print(f"FELICIDADES GANASTE EL NUMERO ERA {number}")
        elif numero>number:
            print(f"EL NUMERO QUE ELIGIO ES MAYOR A {number}")
        else:
            print(f"EL NUMERO QUE ELIGIO ES MENOR A {number}")

humanguess()

def computerGuess():
    number=random.randrange(0,1000)
    bandera=False
    
    while(bandera==False):
        print(number)
        print ("ES TU NUMERO?")
        opc=input("SI / NO ").lower()
        if opc == "no":
            print("Tu numero es mayor o menor al mio?")
            opc2=input("mayor / menor:").lower()
            if opc2 =="menor":
                newNumber = random.randrange(0,number)       
                number=newNumber     
            else:
                newNumber = random.randrange(0,1000)
                number=newNumber
        else:
            bandera=True  

computerGuess()