import turtle


wn = turtle.Screen()
wn.bgcolor("black")


def skip(x,a,b):
    x.penup()
    x.goto(a,b)
    x.pendown()


Sun = turtle.Turtle()
Sun.shape("circle")
Sun.color("red")
Sun.shapesize(1.5,1.5)

b = turtle.Turtle()
b.shape("circle")
b.color("white")
b.shapesize(0.5,0.5)
skip(b,0,-40)
b.lt(40)

c = turtle.Turtle()
c.shape("circle")
c.color("yellow")
c.shapesize(0.6,0.6)
skip(c,40,40)
c.lt(130)

d = turtle.Turtle()
d.shape("circle")
d.color("blue")
d.shapesize(0.7,0.7)
skip(d,60,-50)
d.lt(60)

e = turtle.Turtle()
e.shape("circle")
e.color("orange")
e.shapesize(0.8,0.8)
skip(e,-20,-120)
d.rt(15)

f = turtle.Turtle()
f.shape("circle")
f.color("brown")
f.shapesize(0.9,0.9)
skip(f,10,-130)
f.lt(10)

g = turtle.Turtle()
g.shape("circle")
g.color("purple")
g.shapesize(1,1)
skip(g,0,-200)
g.lt(5)

h = turtle.Turtle()
h.shape("circle")
h.color("blue")
h.shapesize(1.1,1.1)
skip(h,30,-260)

j = turtle.Turtle()
j.shape("circle")
j.color("green")
j.shapesize(1.2,1.2)
skip(j,160,-320)
j.lt(30)


for i in range(120):
    a = 2
    if 0 <= i < 30 or 60 <= i  <90:
        a = a + 0.9
        b.lt(3)
        b.fd(a)
        c.lt(3)
        c.fd(a + 1.4)
        d.lt(3)
        d.fd(a + 2.8)
        e.lt(3)
        e.fd(a + 5)
        f.lt(3)
        f.fd(a + 6)
        g.lt(3)
        g.fd(a + 8)
        h.lt(3)
        h.fd(a +12)
        j.lt(3)
        j.fd(a + 16)
    else:
        a = a - 0.9
        b.lt(3)
        b.fd(a)
        c.lt(3)
        c.fd(a + 1.4)
        d.lt(3)
        d.fd(a + 2.8)
        e.lt(3)
        e.fd(a + 5)
        f.lt(3)
        f.fd(a + 6)
        g.lt(3)
        g.fd(a +8)
        h.lt(3)
        h.fd(a + 12)
        j.lt(3)
        j.fd(a +16)