def add_juice(j_list):
  new = input("輸入果汁:")
  if new in j_list:
    print("已有此果汁")
  else:
     j_list.append(new)
     print("新增完成")
  return j_list

def show_juice(j_list):
  print(j_list)
  return j_list

def remove_juice(j_list):
  r=input('刪除果汁:')
  if r in j_list:
    j_list.remove(r)
    print('成功刪除此果汁')
  else:
    print('無此果汁')
  return j_list


juice_list=[]
fun_list=[add_juice,show_juice,remove_juice]
while True:
    print("1  想加入菜單的果汁")
    print("2  顯示菜單")
    print('3  刪除果汁')
    print("4  結束程式")
    a = int(input("選擇步驟:"))
    if a == 4:
        print("結束程式")
        break
    else:
      juice_list=fun_list[a-1](juice_list)
