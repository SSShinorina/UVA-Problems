t=int(input())
case=0
for i in range(0,t):
    case +=1
    a=list(map(int,input().split()))
 
    if(a[-3]>=a[-2])and(a[-1]>=a[-2]):
        avg=(a[-3]+a[-1])/2
    elif(a[-3]>=a[-1])and(a[-2]>=a[-1]):
        avg=(a[-3]+a[-2])/2
    elif(a[-1]>=a[-3])and(a[-2]>=a[-3]):
        avg=(a[-1]+a[-2])/2
    else:
        exit
    s=int(sum(a[:4])+avg)
    if(s>=90):
        print("Case {0}: A".format(case))
    elif(80<=s<90):
        print("Case {0}: B".format(case))
    elif(70<=s<80):
        print("Case {0}: C".format(case))
    elif(60<=s<70):
        print("Case {0}: D".format(case))
    elif(s<60):
        print("Case {0}: F".format(case))
    else:
        exit
exit
