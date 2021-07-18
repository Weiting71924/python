"""
輸入一數字n為尋找的區間範圍, 找出區間範圍
3,7的倍數顯示在螢幕上，其餘不顯示，可使用取餘數函式%
​
​
e.g.
input:20
output: 
3
6
7
9
12
14
15
18
"""
n=int(input("輸入一個數字:"))
for w in range(n):
  if w%3==0:
    print(w)
  elif w%7==0:
    print(w)