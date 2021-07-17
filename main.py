import turtle as t
t.shape("circle")
t.pensize(3)
t.turtlesize(0.5)
t.pencolor("dodgerblue")
t.stamp()
for e in range(1,360,6):
  t.speed(0)
  t.clear()
  t.forward(90)
  t.home()
  t.right(e)
  import time
  time.sleep(1)