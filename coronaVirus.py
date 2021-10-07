import turtle as t

sc = t.Screen()
sc.title("করোনাভাইরাস (Orthocoronavirinae)")
a = 0
b = 0
t.bgcolor("white")
t.speed(10)
t.pencolor("red")
t.penup()
t.goto(0, 200)
t.pendown()

while True:
    t.forward(a)
    t.right(b)
    a += 3
    b += 1
    if b == 201:
        break
t.close()