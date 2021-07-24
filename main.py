# juice_list = ["1", "2"]
# while True:
#     print("1  想加入菜單的果汁")
#     print("2  顯示菜單")
#     print("3  結束程式")
#     a = input("選擇步驟:")
#     if a == "1":
#         new = input("輸入果汁:")
#         if new in juice_list:
#           print("已有此果汁")
#         else:
#           juice_list.append(new)
#           print("新增完成")
#         # for l in juice_list:
#         #     if new == l:
#         #         print("已有此果汁")
#         #         break
#         # else:
#         #     juice_list.append(new)
#         #     print("新增完成")
#     if a == "2":
#         print(juice_list)
#     if a == "3":
#         print("結束程式")
#         break

import random

num_dice=int(input("輸入骰子數:"))
def roll_dice(n):
  dice=[]
  for i in range(n):
    dice.append(random.randint(1,6))
  return dice
print(roll_dice(num_dice))


