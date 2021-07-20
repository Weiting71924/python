import random as r
a=r.randint(1,100)
bingo=False
while bingo==False:
  n=int(input("輸入密碼:"))
  if n<a:
    print("再大")
  elif n>a:
    print("再小")
  else:
    print("bingo")
    bingo=True

a=[1,2,3]
b=a
b[0]=2
print(a)