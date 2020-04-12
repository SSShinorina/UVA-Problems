for i in range(0,1000):
    a,b,c=map(int,input().split())
    if(a<30000) and (b<30000) and (c<30000):
        if(c>=a) and (c>=b):
            if((a**2+b**2)==c**2):
                print("right")
            else:
                print("wrong")
        exit
    exit
exit

