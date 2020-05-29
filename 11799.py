t=int(input())
case=0
for i  in range(0,t):
  case+=1
  m=map(int,input().split())
  n=list(m)
  print("Case {0}: {1}".format(case,max(n)))
exit
