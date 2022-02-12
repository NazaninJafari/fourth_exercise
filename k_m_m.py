
def kmm(x , y):

    if x>y :
        max = x
    else:
        max = y    

    for i in range(1,max) :
        if (max % x)==0 and (max % y)==0 :
            print("kmm: ",max)
            break

        max=max*i

x = int(input("Enter number 1: "))
y = int(input("Enter number 2: "))

kmm(x , y);    