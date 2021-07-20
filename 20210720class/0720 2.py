import random as r
n=int(input("輸入密碼:"))
a=r.randint(1,10)
if n<a:
  print("再大")
elif n>a:
  print("再小")
else:
  print("bingo")