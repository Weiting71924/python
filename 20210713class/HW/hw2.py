import turtle as t
t.stamp()
t.penup()
for f in range(1, 360, 45):
    t.right(f)
    t.forward(90)
    t.stamp()
    t.home()