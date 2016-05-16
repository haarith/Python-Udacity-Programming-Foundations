import turtle

def draw_square(some_turtle):
    for i in range(1,5):
        some_turtle.forward(100)
        some_turtle.right(90)

def draw_art():
    window = turtle.Screen()
    window.bgcolor("green")

    #Create the turtle Haris - draws a square
    haris = turtle.Turtle()
    haris.shape("turtle")
    haris.color("blue")
    haris.speed(1)
    draw_square(haris)
    
    #Create the turtle Beg - draws a circle
    beg = turtle.Turtle()
    beg.shape("arrow")
    beg.color("red")
    beg.circle(100)

    window.exitonclick()

draw_art()
