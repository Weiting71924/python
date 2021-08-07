import random
import time
def update_life(st):
    get_life = random.randint(1, 3)
    st[1] += get_life
    print('\n發現紅藥水!!!!')
    print('獲得HP:{}, 目前HP:{}'.format(get_life, st[1]))
    return st

def update_money(st):
    get_money = random.randint(50, 200)
    st[2] += get_money
    print('\n撿到$$')
    print('獲得${}, 擁有${}'.format(get_money, st[2]))
    return st

def store(st):
  print('遇到商店')
  print('  請選擇商品')
  print('a  醫療包(HP+2)    $400')
  print('b  醫療箱(HP+6)    $1100')
  print('c  匕首(物攻+2)    $500')
  print('d  法杖(魔攻+2)    $500')
  print('e  不購買')
  w=input('輸入代號:')
  if w=='a':
    if st[2]<400:
      print('餘額不足')
      return st
    else:
      st[2]-=400
      st[1]+=2
  elif w=='b':
    if st[2]<1100:
      print('餘額不足')
      return st
    else:
      st[2]-=1200
      st[1]+=6
  elif w=='c':
    if st[2]<500:
      print('餘額不足')
      return st
    else:
      st[2]-=500
      st[4]+=2
  elif w=='d':
    if st[2]<500:
      print('餘額不足')
      return st
    else:
      st[2]-=500
      st[5]+=2
  else:
    print('離開商店')
  return st

def fight(st):
    monsterHP=random.randint(2,20)
    monsteratt=random.randint(2,6)
    p_att=random.randint(1,3)
    get_money=random.randint(100,400)
    p_attM=random.randint(4,10)
    print('\n遇到怪物  HP:{}'.format(monsterHP))
    print('!!!!戰鬥開始!!!!')
    while True:
      time.sleep(1)
      print('\n玩家攻擊')
      print('a  物攻')
      print('b  魔攻')
      e=input('攻擊模式:')
      if e=='a':
        print('造成{}點傷害'.format(p_att+st[4]))
        monsterHP-=p_att+st[4]
      elif e=='b':
        if st[3]==0:
          print('魔力不足')
        else:
          st[3]-=1
          print('造成{}點傷害'.format(p_attM+st[5]))
          monsterHP-=p_attM+st[5]
      print('怪物剩餘HP:{}'.format(monsterHP))
      if monsterHP<=0:
        print('\n擊敗怪物!!!!!')
        st[2]+=get_money
        print('獲得${}'.format(get_money, st[2]))
        return st
      time.sleep(1)
      print('\n怪物攻擊')
      print('玩家剩餘HP:{}'.format(st[1]))
      st[1]-=monsteratt
      if st[1] <= 0:
        st[0] = 0
        return st
      else:
        continue

def rfile():
    f = open("output", 'r')
    st = []
    for line in f:
        st.append(int(line))
    f.close()
    return st

def wfile(st):
    f = open("output.txt", 'w')
    for i in st:
        f.write("{}\n".format(i))
    f.close()

status = [1, 10, 1000,10,0,0]#生死,HP,$$,MP,物攻,魔攻
func_list = [update_life, update_money, fight,store]
while True:
    case = random.randrange(0, len(func_list))
    status = func_list[case](status)
    print("玩家狀態 = {}".format(status))
    time.sleep(1.5)
    if status[0] == 0:
        print("Game Over !!")
        break