import random

num_dice=int(input("輸入骰子數:"))
def roll_dice(n):
  dice=[]
  for i in range(n):
    dice.append(random.randint(1,6))
  return dice
print(roll_dice(num_dice))