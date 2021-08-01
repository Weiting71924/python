'''
20210731
作業
請使用def畫出10個，不同顏色的屋頂、房身，及位置的房子
顏色用list用代入
'''
import turtle as t
import random
def h_t(x,y):
  t.color('red')
  t.penup()
  t.goto(x,y)
  t.pendown()
  t.begin_fill()
  t.right(45)
  t.forward(30)
  t.right(135)
  t.forward(30*1.414)
  t.right(135)
  t.forward(30)
  t.setheading(0)
  t.end_fill()
def h_b(x,y):
  t.color('red')
  t.penup()
  t.goto(x-15,y-15*1.414)
  t.pendown()
  t.begin_fill()
  for e in range(4):
    t.forward(30)
    t.right(90)
  t.end_fill()
t.hideturtle()
def color():
  

n=20
xy_range=100
for o in range(n):
  x=random.randint(-xy_range,xy_range)
  y=random.randint(-xy_range,xy_range)
  h_t(x,y)
  h_b(x,y)



