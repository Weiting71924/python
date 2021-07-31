import random
import time


def update_life(st):
    get_life = random.randint(1, 3)
    st[1] += get_life
    print('\n發現紅藥水!!!!')
    print('獲得HP:{}, 目前HP:{}'.format(get_life, st[1]))
    return st


def update_money(st):
    get_money = random.randint(10, 30)
    st[2] += get_money
    print('\n撿到$$')
    print('獲得${}, 擁有${}'.format(get_money, st[2]))
    return st


def fight(st):
    print('\n遇到怪物')
    monsterHP=random.randint(2,10)
    p_att=random.randint(1,3)
    get_money=random.randint(10,20)
    print('戰鬥開始!!!!')
    while True:
      print('玩家攻擊，造成{}點傷害'.format(p_att))
      monsterHP-=p_att
      print('怪物攻擊')
      st[1] -= 1
      if monsterHP<=0:
        print('擊敗怪物!!!')
        st[2]+=get_money
        return st
        break
      if st[1] <= 0:
          st[0] = 0
      return st


status = [1, 10, 0]
func_list = [update_life, update_money, fight]
while True:
    case = random.randrange(0, len(func_list))
    status = func_list[case](status)
    print("玩家狀態 = {}".format(status))
    time.sleep(1)
    if status[0] == 0:
        print("Game Over QAQ!!")
        break
