t=int(input())

case=0
for i in range(0,t):
    case +=1
    n=int(input())
     
    a=list(map(int,input().split()))
    h=0
    l=0
    for k in range(1,len(a)):
        if(a[k-1]<a[k]):
            h +=1
        elif(a[k-1]>a[k]):
            l +=1
        exit
    print("Case {0}: {1} {2}".format(case,h,l))
    exit
      
exit
