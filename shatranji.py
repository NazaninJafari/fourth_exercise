def chatranji(n,m) :
    
    a=0
    while n>0 :
        
        i=0
        for i in range(0,m):
            
            if (a % 2)==0 :
                print("#", end='')
                
            elif (a % 2)==1 :
                print("*", end='')
            a+=1
            
        if (m%2)==1 :
            a+=2
        else:
            a+=1
        n-=1    
        print("\r") #boro sare khat
        

n=int(input("n: "))
m=int(input("m: "))
chatranji(n,m);    