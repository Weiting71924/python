a=int(input("請輸入箭頭大小:"))
for i in range(1,a+1):
  print(("*"*(2*i-1)).center(a*2-1))
for s in range(a):
  w=" "*(a-1)+"*"
  print(w)




# for r in range(1,a+1):
#   val="0"*r
#   print(val)
# i=a-1
# while i>=0:
#   print("0"*i)
#   i-=1
# for f in range(1,a*2,2):
#   t="*"*f
#   print((t).center(a*2-1))