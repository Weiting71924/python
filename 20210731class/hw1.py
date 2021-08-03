'''
20210731
作業
請使用def畫出10個，不同顏色的屋頂、房身，及位置的房子
顏色用list用代入
'''
import turtle as t
import random
def h_t(x,y,color):
  t.color(color)
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
def h_b(x,y,color):
  t.color(color)
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
  r=random.randint(0,255)
  g=random.randint(0,255)
  b=random.randint(0,255)
  color=(r/255,g/255,b/255)
  return color
  

n=10
xy_range=101
for o in range(n):
  x=random.randrange(-xy_range,xy_range,30)
  y=random.randrange(-xy_range,xy_range,30)
  h_t(x,y,color())
  h_b(x,y,color())
