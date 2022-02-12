#moadele daraje 2
from cmath import sqrt
import math

def moadele_daraje2(a,b,c):
    

    delta = (b**2) - (4*a*c)

    if delta < 0 :
        print("not defined!!")
        exit

    elif delta == 0 :
        x = -b / (2*a) 
        print("x= " ,x)
        exit

    elif delta > 0 :

        i2= math.sqrt(delta)
        x1 = ((-b) - i2) / (2 * a)
        x2 = ((-b) + i2) / (2 * a)

        print ("x1= ",x1)
        print ("x2= ",x2)

a= float(input("a = "))
b= float(input("b = "))
c= float(input("c = "))
moadele_daraje2(a,b,c);
