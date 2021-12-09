import turtle

t = turtle.Turtle()
window = turtle.Screen()
t.penup()
t.pendown()

#letter I
t.pensize(15)
t.pencolor("yellow")
t.speed(1)
t.forward(20)
t.backward(40)
t.forward(20)
t.right(90)
t.forward(50)
t.left(90)
t.forward(20)
t.backward(40)

#letter C
t.penup()
t.goto(100,-45)
t.pendown()
t.speed(1)
t.color("orange") 
t.circle(30, -180)

#letter H
t.color("red")
t.penup()
t.goto(145,-20)
t.pendown()
t.speed(1)
t.right(90)
t.forward(30)
t.backward(60)
t.forward(30)
t.right(90)
t.forward(30)
t.left(90)
t.forward(30)
t.backward(60)

#letter A
t.color("black")
t.right(85)
t.penup()
t.goto(230,-20)
t.pendown()
t.speed(1)
t.forward(60)
t.right(45)
t.forward(25)
t.backward(65)
t.right(90)
t.forward(75)

#drawingFlower1
t.penup()
t.goto(-200,-40)
t.pendown()
t.fillcolor('pink')
t.begin_fill()
for i in range(5):
    t.circle(38,180)
    t.right(108)
t.end_fill()
t.up()
t.goto(-140,-30)
t.down()
t.color('purple')
t.dot(48)

#drawingFlower2
t.penup()
t.goto(450,-40)
t.pendown()
t.fillcolor('pink')
t.begin_fill()
for i in range(5):
    t.circle(38,180)
    t.right(108)
t.end_fill()
t.up()
t.goto(510,-30)
t.down()
t.color('purple')
t.dot(48)

window.exitonclick()


