i=int(input("Enter the number,i:"))
j=int(input("Enter the number,j:"))
print (i,j)
for num in range(i,j):
    def count(num):
        count = 0
    
        if num > 0:
            count = count+1
            if num==1:
                return 1
            elif num%2==0:
                return(3*num+1)
            else:
                return(num/2)
        return count


print(i, j,count(num))

exit








