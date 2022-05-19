from paddle import Paddle
from turtle import Screen,Turtle
from ball import Ball
from scoreboard import Scorebd
import time
s=Screen()
s.bgcolor('black')
s.setup(width=800,height=600)
s.title('pong')
s.tracer(0)
s.listen()
rpaddle=Paddle((380,0))
lpaddle=Paddle((-380,0))
ball=Ball()
s.onkey(rpaddle.go_up,'Up')
s.onkey(rpaddle.go_down,'Down')
s.onkey(lpaddle.go_up,'w')
s.onkey(lpaddle.go_down,'s')
scbd=Scorebd()
is_on=True
x=0.1
while is_on:
    time.sleep(x)
    s.update()
    ball.move()
    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bouncey()
    elif ball.distance(rpaddle)<50 and ball.xcor()>340 or ball.distance(lpaddle)<50 and ball.xcor()<-340:
        ball.bouncex()
        x*=0.9
    elif ball.xcor()>380:
        ball.reset_pos()
        x=0.1
        ball.bouncex()
        scbd.r_point()
    elif ball.xcor()<-380:
        ball.reset_pos()
        x=0.1
        ball.bouncex()
        scbd.l_point()
        
s.exitonclick()