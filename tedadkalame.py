def count(string):
    x = 1
    i = 0

    while i < len(string) :
        if string[i]== ' ' :
            x+=1
        i+=1

    print(x)    

string = input("write somthing: ")
count(string) ;       
