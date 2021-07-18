"""
輸入一數字n為尋找的區間範圍, 找出區間範圍
的質數顯示在螢幕上，其餘不顯示。
​
​
"""
n=int(input("輸入一數字:"))
for e in range(2,n+1):
  i=2
  c=0
  while i<e:
    if e%i==0:
      c=1
    i+=1
  if c==0:
    print(e)




