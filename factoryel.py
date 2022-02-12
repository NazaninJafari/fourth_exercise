from tkinter import N

def facto(x):

    a=1
    c=1
    while c<=x:
        c = c*a
        if c==x :
            print("yes")
            break
        a+=1 

    if c>x :
        print("No")

x=int(input("enter your number: "))
facto(x);