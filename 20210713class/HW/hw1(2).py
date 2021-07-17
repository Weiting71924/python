a = int(input("請輸入箭頭大小:"))
for r in range(1, a + 1):
    val = " " * (a - r) + "*" * (r * 2 - 1)
    print(val)
for e in range(a):
    print(" " * (a - 1) + "*")