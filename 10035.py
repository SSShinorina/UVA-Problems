##while True:
##  m,n=map(int,input().split())
##  cnt=0
##  c=0
##  if(m==0 and n==0):
##    break
##  for i in range(10):
##    c=m%10+n%10
##    if (c>9):
##      c=1
##    else:
##      c=0
##    cnt+=c
##    m/=10
##    n/=10
##    
##  if(cnt==0):
##    print("No carry operation.")
##  elif(cnt==1):
##    print("1 carry operation.")
##  else:
##    print("{0} carry operations.".format(cnt))


while True:
  m,n=map(int,input().split())
  count=0
  s=0
  if(m==0 and n==0):
    break
  add=m+n
  add=list(str(add))
  for i in range(len(add)):
    if(add[i]=='1'):
      s=1+s
    else:
      exit
  count+=s
  if(count==0):
    print("No carry operation.".format(count))
  elif(count==1):
    print("1 carry operation.")
  else:
    print("{0} carry operations.".format(count))
  exit
exit
  
 
   
    

