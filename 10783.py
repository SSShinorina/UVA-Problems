number=input("Enter the maximum number:")
number1=input("Enter the minimum number:")
case=input("Enter the case:")
array=list(range((int (number1)),(int (number))))
odd=sum([i for i in array if i%2 !=0])
print(array)
print ("Case",case,":",odd)
 
exit
