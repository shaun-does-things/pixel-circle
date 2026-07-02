import turtle

def MCA(r,yn):
    # define variables (coords and the other bs)
    p = 1 - r
    x = 0
    y = r
    values = []
    # the "if then" bit
    while x < y:
        if p < 0:
            p = p+(2*x)+3
            x = x+1
            values.append((x, y))
        else:
            p = p+(2*(x-y))+5
            x = x+1
            y = y-1
            values.append((x, y))
    print(values)
    # the fuckass turtle bit (i dont even know how turtle works T^T
    # making it "pwetty :3" by drawing a huge +
    def pwetty():
        for y in range(-r,r+1):
            turtle.goto(0,y*10)
            squaremaxxing()
        for x in range(-r,r+1):
            turtle.goto(x*10,0)
            squaremaxxing()
    # squaremaxxing
    def squaremaxxing():
        turtle.pendown()
        turtle.setheading(0)
        for i in range(4):
            turtle.forward(10)
            turtle.right(90)
        turtle.penup()
    # making the circle instead of 1/8 of a circle
    def diabeto(x, y):
        pts = [
            ( x,  y), ( y,  x),
            (-x,  y), (-y,  x),
            (-x, -y), (-y, -x),
            ( x, -y), ( y, -x),
        ]
        for px, py in pts:
            turtle.goto(px * 10, py * 10)
            squaremaxxing()
    # actually making the turtle do things
    if yn == "ye":
        # init turtle
        turtle.speed(0)
        turtle.color("black")
        # drawing
        turtle.penup()
        for xt,yt in values:
            diabeto(xt,yt)
        pwetty()
        turtle.Screen().exitonclick()
    elif yn == "fast":
        # init turtle
        turtle.speed(0)
        turtle.delay(0)
        turtle.tracer(0,0)
        turtle.color("black")
        # drawing
        turtle.penup()
        for xt,yt in values:
            diabeto(xt,yt)
        pwetty()
        turtle.update()
        turtle.Screen().exitonclick()
    else:
        balls = 2
radius = int(input("radius?"))
yena = input("do you want it drawn by turtle, and do you want instant mode? [ye/na/fast]")
MCA(radius,yena)