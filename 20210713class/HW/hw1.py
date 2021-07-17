a=int(input("請輸入箭頭大小:"))
for i in range(1,a+1):
  print(("*"*(2*i-1)).center(a*2-1))
for s in range(a):
  w=" "*(a-1)+"*"
  print(w)
