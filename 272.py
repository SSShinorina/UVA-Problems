c=0
while True:
  try:
    array=str(input())
  except EOFError:
    break
  a=[]
  for i in array:
    if i=='"':
      if c==0:
        a.append("``")
        c=1
      else:
        a.append("''")
        c=0
      exit
    else:
      a.append(i)
    exit
  print("".join(a))
  exit
exit
    
   
##  if(i%2==0):
##    if(array[i]=='"'):
##      print(array.append('``'),end='')
##    else:
##      print(array)
##  elif(i%2==1):
##    if(array[i]=="'"):
##      print(array.append("''"),end='')
##    else:
##       print(array,end='')
##  else:
##    print(array,end='')
exit
  
    ##  val=str(array.index(i))
####  if(val=='"'):
####    if(i%2==1):
####      a=array.replace('"','``')
####    elif(i%2==0):
####      a=array.replace('"','Hi')
####    else:
##
####      a=array
## 
##  if(i%2==1):
####    if(val=='"'):
####    a=array.replace(val,'``')
####    else:
####      print(array,end='')
##    print('Hi')
##  elif(i%2==0):
####    if(val=='"'):
##    a=array.replace(val,"''")
####    else:
####      print(array,end='')
##  else:
##    exit
##    
##print(a,array,end='')

 
  
 


 

