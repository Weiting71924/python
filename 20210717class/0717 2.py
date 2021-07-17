import random as r
print(r.randint(0, 5))
print(r.randrange(1, 20,2))

l = int(input("輸入長度:"))
a = 0
while l >= 20:
    l /= 2
    a += 1
else:
    print("需對折" + str(a) + "次")