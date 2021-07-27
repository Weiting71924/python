'''
讓使用者輸入一個str，當str有在list裡面，就移除該str
沒有str就加入list, 並顯示最後的list，list初使值為
["apple", "ball" ,"car"]
'''



l=["apple", "ball" ,"car"]
while True:
  s=input("\n輸入一個單字:")
  if s in l:
    l.remove(s)    
  else:
    l.append(s)
  print(l)