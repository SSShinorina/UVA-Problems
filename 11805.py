t=int(input())
case=0
for i in range(0,t):
  case+=1
  a,b,c=map(int,input().split())
  o=(b+c)%a
  if(o==0):
    print("Case {0}: {1}".format(case,a))
  else:
    print("Case {0}: {1}".format(case,o))
  exit
exit
