t=int(input())
sum=0
for i in range(t):
    a=list(map(str,input().split()))
    if(a[0]=='donate'):
        b=int(a[1])
        sum+=b
    elif(a[0]=='report'):
        print(sum)
    exit
exit
    

