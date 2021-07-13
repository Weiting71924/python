import turtle as tur
tur.color("red")
tur.shape("circle")
tur.penup()
for q in range(1,120,3):
  tur.forward(q)
  tur.right(35)
  tur.stamp()
  print(q)

import turtle as t
t.fillcolor("yellow")
t.pencolor("red")
t.pensize(6)
t.begin_fill()
for g in range(5):
  t.forward(150)
  t.right(144)
t.end_fill()
t.speed(0)
import time
time.speed(5)