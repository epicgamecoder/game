import turtle as t
import random
import winsound
import time
wn = t.Screen()
wn.setup(500,500)
wn.bgcolor("black")
mypen = t.Turtle()

xcoord = random.randrange(-220,220,20)
ycoord = random.randrange(-220,220,20)

#ball
ball = t.Turtle()
ball.fd(3)
ball.rt(2)
ball.hideturtle()
ball.shape("circle")
ball.color("red")
ball.penup()
ball.goto(xcoord,ycoord)
ball.showturtle()

#player
player = t.Turtle()
player.penup()
player.dx = 0.5
player.dy = 0.5
player.shape("triangle")
player.color("blue")
def up():
    y = player.ycor()
    y += 20
    player.sety(y)
def down():
    y = player.ycor()
    y -= 20
    player.sety(y)
def left():
    x = player.xcor()
    x -= 20
    player.setx(x)
def right():
    x = player.xcor()
    x += 20
    player.setx(x)
score = 0    
    
wn.listen()
wn.onkeypress(up,"Up")
wn.onkeypress(down,"Down")
wn.onkeypress(left,"Left")
wn.onkeypress(right,"Right")

    
starting_time = time.time()
time_limit = 30

while (time.time() - starting_time) < time_limit:
    wn.update()
    player.fd(5)
    player.lt(5)
    

    if player.xcor()>235:
        player.setx(210)
    if player.xcor()<-235:
        player.setx(-210)
    if player.ycor()>235:
        player.sety(210)
    if player.ycor()<-235:
        player.sety(-210)
    if player.distance(ball) < 20:
        winsound.Beep(1000,250)
        a = random.randint(-220,220)
        b = random.randint(-220,220)
        ball.hideturtle()
        ball.goto(a,b)
        ball.showturtle()
        mypen.undo()
        score += 1
        mypen.setposition(-220,220)
        mypen.hideturtle()
        mypen.color("white")
        mypen.pendown()
        mypen.write(f"Score:{score} ",align = "left",font = ("Arial",10,"normal"))
    if (time.time() - starting_time) > time_limit:
        winsound.Beep(500,500)
        wn.bye()
        input(f"""In thirty seconds,
Your score was {score}""")





wn.mainloop()


