n=int(input())
case=0
for i in range (0,n):
    a,b,c=map(int,input().split())
    case +=1
    if(a<b<c) or (a>b>c):
        print("Case {0}: {1}".format(case,b))
    elif(b<a<c) or (b>a>c):
        print("Case {0}: {1}".format(case,a))
    else:
        print("Case {0}: {1}".format(case,c))

           
exit


