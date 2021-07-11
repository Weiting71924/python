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