'''
作業
使用者輸入兩個數num1 and num2，
並使用function def 求最小公倍數
value = lcm(num1, num2)
'''
def lcm(n1,n2):
  if n1>n2:
    b=n1
  else:
    b=n2
  for a in range(b,n1*n2+1):
    if a%n1==0 and a%n2==0:
      lcm=a
      break
  return lcm
num1=int(input('輸入一個數:'))
num2=int(input('輸入一個數:'))
print(lcm(num1, num2))