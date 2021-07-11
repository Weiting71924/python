"""
Topic:輸入三角形三邊，判斷是否能構成三角形，
　　　是三角形則顯示面積和周長，不行則顯示，無法構成三角形:
​
Triangle Area formula: 
p = 1/2 (a+b+c)
area = (p * (p - a) * (p - b) * (p - c)) ** 0.5
​
e.g.
Show:a ="
Input1:3
​
Show:b ="
Input2:4
​
Show:c ="
Input3:5
​
output:
perimeter: 12.000000
Area: 6.000000
"""

print("請輸入三角形三邊")
a = float(input("\n其一:"))
b = float(input("\n其二:"))
c = float(input("\n其三:"))
s = (a + b + c) * (1 / 2)
perimeter=a+b+c
area = (s * (s - a) * (s - b) * (s - c))**0.5
if a+b-c > 0:
    print("\n面積:{0:.3f}".format(area))
    print("\n周長:{0:.2f}".format(perimeter))
else:
    print("\n數據錯誤")
print("\n程式結束")