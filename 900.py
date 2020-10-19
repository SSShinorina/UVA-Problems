##while True:
##  i=int(input())
##  l=[1,1,2]
##  if i==0:
##    break
##  else:
##    for n in range(3,50):
##      l.append(2*l[n-1]+l[n-2])
##    print(l[n])
##exit
     
l = [1,1,2,3]
for i in range(4,56):
  l.append(2*l[i-2]+l[i-3])
while True:
  n=int(input())
  if n==0:
    break
  else:
    print (l[n])
		 
  
