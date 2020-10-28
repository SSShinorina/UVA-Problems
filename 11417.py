import math
while True:
  i=int(input())
  g=0
  if i==0:
    break
  for a in range(1,i):
    for b in range(a+1,i+1):
      g=g+math.gcd(a,b)
    exit
  exit
  print(g)
exit
