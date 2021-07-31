import turtle as t
import random
def tree_l(x,y,color):
  t.penup()
  t.goto(x,y)
  t.pendown()
  t.setheading(0)
  t.color(color)
  t.begin_fill()
  for a in range(2):
    t.forward(40)
    t.left(120)
  t.end_fill()
def tree_t(x,y,color):
  t.penup()
  t.goto(x+28,y)
  t.pendown()
  t.color(color)
  t.begin_fill()
  t.setheading(0)
  for b in range(2):
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(20)
  t.end_fill()
def randcolor():
  r=random.randint(0,255)
  g=random.randint(0,255)
  b=random.randint(0,255)
  color=(r/255,g/255,b/255)
  return color

n=20
xy_range=50
for o in range(n):
  x=random.randint(-xy_range,xy_range)
  y=random.randint(-xy_range,xy_range)
  tree_l(x,y,randcolor())
  tree_t(x,y,randcolor())
