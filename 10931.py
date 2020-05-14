def countSetBits(num): 
   
     binary = bin(num)
    
   
     setBits = [ones for ones in binary[2:] if ones=='1']
     print("The parity of {0} is {1} (mod 2).".format(binary[2:],len(setBits)))
    
 
if __name__ == "__main__":
    while True:
        num = int(input())
        if num == 0:
                  break
        countSetBits(num)
    exit
exit
