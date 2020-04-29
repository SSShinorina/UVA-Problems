n=int(input())
case=0
for i in range (0,n):
    m=int(input())
    case +=1
    if(-1000 <= m) and (m <=1000):
            m=(((((m*567)/9)+7492)*235)/47)-498
             
            m=int(m)
            X = str(m)
            l = len(X)
            print(X[l-2])
    exit         
 
exit


