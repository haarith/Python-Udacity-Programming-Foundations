import turtle

def draw_square():
    window = turtle.Screen()
    window.bgcolor("green")
    
    haris = turtle.Turtle()
    haris.shape("turtle")
    haris.color("blue")
    haris.speed(1)
    
    haris.forward(100)
    haris.right(90)
    haris.forward(100)
    haris.right(90)
    haris.forward(100)
    haris.right(90)
    haris.forward(100)
    haris.right(90)

    beg = turtle.Turtle()
    beg.shape("arrow")
    beg.circle(100)

    window.exitonclick()


draw_square()
