import math
t=int(input())
pi=math.acos(-1)
for i in range(0,t):
  l=int(input())
  wid=l*0.60
  radius=l/5
  red=pi*radius*radius
  green=l*wid-red
  print("%.2f"%red,"%.2f"%green)
exit
