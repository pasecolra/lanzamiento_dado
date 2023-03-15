
import random

# input

# processing

d1= random.randint(1,6)
# d2= random.randint(1,6)

d2=int(input("adivina el numero del dados"))

"""if (d1==1):
    rta= "UNO"
elif (d1==2):
    rta= "DOS"
elif (d1==3):

    rta= "TRES"
elif (d1==4):
    rta= "CUATRO"
elif (d1==5):
    rta= "CINCO"
elif (d1==6):
    rta= "SEIS"
else:
    rta="no es la cara de un dado"""

if d2>6:
    print("USTED DIGITO UN NUMERO NO VALIDO")

else:
    if (d1==d2):
        rta="ADIVINASTE"
    else:
        rta="NO ADIVINASTE"

    # output
    print(rta)
    print("dado: " + str(d1))
    print("USTED DIGITO: " + str(d2))