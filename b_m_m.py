from tkinter import Y


def bmm(x , y) :

    if x < y :
        m = x
    else :
        m = y


    for i in range(1 , m) :
        if (x % m)==0 and (y % m)==0 :
            
            print("bmm: ",m)
            break
        else:
            m-=1
        
x = int(input("Number 1: "))
y = int(input("Number 2: "))

bmm(x , y);
