import random as r
n=int(input("輸入範圍:"))
a=r.randint(1,n)
for t in range(1,n+1):
  if a==t:
    print(t)
  else:
    continue