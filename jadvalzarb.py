
def jadvalzarb(n,m) :
    
    a = 1
    b = 1
    i=0
    while a <= n :
        for i in range(m) :
            c = a*b
            print(c , end="")
            print("\t", end="") #fasele beyn aadad
            b+=1
        print("\r") #boro sare khat
        a+=1
        b=1

n = int(input("n= "))
m = int(input("m= "))

jadvalzarb(n,m);

