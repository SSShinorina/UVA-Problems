##t=10
##for i in range(t):
##    x=int(input())
##    for j in range(x):
##        ans=int((x * x * (x + 1) * (x + 1)) / 4);
##   
##    print(ans)
##    exit
##exit
## 
while True:
    try:
        x=int(input())
        for j in range(x):
            ans=int((x * x * (x + 1) * (x + 1)) / 4);
        print(ans)
        exit
        
    except EOFError:
        break
exit
    
 
  
