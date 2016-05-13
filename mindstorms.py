import turtle

def draw_square():
    window = turtle.Screen()
    window.bgcolor("green")
    
    haris = turtle.Turtle()
    haris.forward(100)
    haris.right(90)
    haris.forward(100)
    haris.right(90)
    haris.forward(100)
    haris.right(90)
    haris.forward(100)
    haris.right(90)

    window.exitonclick()


draw_square()
