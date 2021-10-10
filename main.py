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
    bandera=False
    minNumber=0
    maxNumber=100
    number=random.randrange(minNumber,maxNumber)
    
    while(bandera==False):
        print(number)
        print ("ES TU NUMERO?")
        opc=input("SI / NO ").lower()
        if opc == "no":
            print("Tu numero es mayor o menor al mio?")
            opc2=input("mayor / menor:").lower()
            if opc2 =="menor":
                maxNumber=number
                newNumber = random.randrange(minNumber,maxNumber)       
                number=newNumber     
            else:
                minNumber=number
                newNumber = random.randrange(minNumber,maxNumber)
                number=newNumber
        else:
            bandera=True  
            print ("GANASTE")

computerGuess()