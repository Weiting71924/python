"""
Topic:請使用input輸入要印制的箭頭大小
可利用字串乘法
e.g.
val="*" * 3
print(val)
***
​
​
1.Show:Please in row: 
2.input:3
  *  
 *** 
*****
  *  
  *  
  * 
"""
a = int(input("請輸入箭頭大小:"))
# b="*"*a

# for j in range(1,a):
#   print(b)

# val=" "*(a-1)+"*"
# for q in range(a):
#   print(val)

# for j in range(9):
#   print("hi")
for k in range(a):
  for n in range(1, a, 2):
    v = " " * (a - k) + "*" * n
    print(v)
