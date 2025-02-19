from commonFunc import *
import random

def classique():
    solde = 100
    choice = ["d1", "d2"]
    x = 1
    i = 0
    while True:
        if solde > 110:
            return True
    # Nombre aléatoire
        rand = random.randint(0, 36)

        # Bet
        if (solde > x*6):
            solde-= x*6
        else:
            return False
        # Verifiy
        if verifyChoice(choice, rand):
            solde += 9*x
            x = 1
        else:
            x*=3
        
        i += 1
        #print("i : "+ str(i)+ " | " + "solde : " + str(solde) + " |  bet : " + str(choice) + " | spin : " + str(rand))


def classiqueRandom():
    solde = 100
    choice = ["d1", "d2"]
    x = 1
    i = 0
    while True:
        if solde > 110:
            return True
    # Nombre aléatoire
        rand = random.randint(0, 36)

        # Bet
        if (solde > x*6):
            solde-= x*6
        else:
            return False
        # Verifiy
        if verifyChoice(choice, rand):
            solde += 9*x
            x = 1
        else:
            choice = random.sample(["d1", "d2", "d3"], 2)
            x*=3
        
        i += 1
        #print("i : "+ str(i)+ " | " + "solde : " + str(solde) + " |  bet : " + str(choice) + " | spin : " + str(rand))


def classiqueRN():
    solde = 100
    choice = ["r"]
    x = 1
    i = 0
    while True:
        if solde > 130:
            return True
    # Nombre aléatoire
        rand = random.randint(0, 36)

        # Bet
        if (solde > x*2):
            solde-= x*2
        else:
            return False
        # Verifiy
        if verifyChoice(choice, rand):
            solde += 6*x
            x = 1
        else:
            x*=2
        
        i += 1
        #print("i : "+ str(i)+ " | " + "solde : " + str(solde) + " |  bet : " + str(choice) + " | spin : " + str(rand))


def classiqueRNCustom():
    solde = 100
    choice = ["r"]
    x = 1
    i = 0
    while True:
        if solde > 150:
            return True
    # Nombre aléatoire
        rand = random.randint(0, 36)
        # Bet
        if (solde > x*2):
            solde-= x*2
        else:
            return False
        # Verifiy
        if verifyChoice(choice, rand):
            solde += 4*x
            if x>2:
                x -= 1
            else:
                x=1
        else:
            x+=1
        
        i += 1
        #print("i : "+ str(i)+ " | " + "solde : " + str(solde) + " |  bet : " + str(choice) + " | spin : " + str(rand))
