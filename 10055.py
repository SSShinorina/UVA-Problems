a, b = map(int, input().split())
if(a<b):
    if(a<2**32) and (b<2**32):
        print(b-a)
else:
    print("Invalid Input")


exit
