while True:
  try:
    a=float(input('輸入數字'))
    b=float(input('輸入數字'))
    print('a/b= '+str(a/b))
    break
  except:
    print('錯誤,請輸入數字')
