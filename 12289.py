w=int(input())
for i in range(w):
    a=str(input())
    l=len(a)
    if((a[0]=='o' and a[2]=='e')
       or(a[0]=='o' and a[1]=='n')
       or(a[1]=='n' and a[2]=='e')):
        print(1)
    elif((a[0]=='t' and a[2]=='o')or
    (a[0]=='t' and a[1]=='w')or
    (a[1]=='w' and a[2]=='o')):
        print(2)
    elif(l==5):
        print(3)
    exit
exit

