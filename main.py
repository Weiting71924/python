"""
Topic:輸入溫度，如果溫度>=40度C,顯示: 太熱, 
　　　如果溫度<= 10 顯示:太冷, 其他：舒適:
​
Show:Please input temperature:"
Input1:40
Output:It's too hot.
"""

t = float(input("溫度(℃ ):"))
if t >= 40:
    print("\n太熱")
elif t <= 10:
    print("\n太冷")
else:
    print("\n舒適")
