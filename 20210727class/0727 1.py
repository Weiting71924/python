import random

def who_is_winner(usr_list, cmp_list):
    usr = sum(usr_list)
    cmp = sum(cmp_list)
    print('usr score %d' % usr)
    print('cmp score %d' % cmp)
    if usr > cmp:
        print('user is winner')
    elif usr < cmp:
        print('compuetr is winner')
    else:
        print('tie')


def roll_dice(n):
    dice = []
    for i in range(n):
        dice.append(random.randint(1, 6))
    return dice


num_dice = int(input("輸入骰子數:"))
# print('roll_dice={}'.format(roll_dice(num_dice)))
user = (roll_dice(num_dice))
comp = (roll_dice(num_dice))
who_is_winner(user, comp)
