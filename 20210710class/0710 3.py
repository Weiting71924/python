word = input("請輸入密碼:")
if word == "6666":
    print("歡迎光臨")
elif word=="8888":
    print("You are VIP")
else:
    print("錯誤")
print("程式結束")


a = int(input("請輸入成績:"))
if a >= 90:
    print("優")
elif a >= 80:
    print("甲")
elif a >= 70:
    print("乙")
elif a >= 60:
    print("丙")
else:
    print("丁")