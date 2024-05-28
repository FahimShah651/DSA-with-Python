

def square_turtle(n,m):

    import turtle             # allows us to use the turtles library
    wn = turtle.Screen()      # creates a graphics window
    wn.bgcolor("lightgreen")        # set the window background color

    Fahim = turtle.Turtle()    # create a turtle named Fahim
    Fahim.color("blue")              # make tess blue
    Fahim.pensize(3)                 # set the width of her pen
    Fahim.speed(10)

    def room():
        for i in range(0, 4):
            Fahim.left(90)
            Fahim.forward(m)

    def seq():
        for i in range(0, n):
            Fahim.forward(m)
            room()

    for i in range(0, 4):
        seq()
        Fahim.left(90)
        Fahim.forward(m)

    # Fahim.stamp()                # leave an impression on the canvas
    # Fahim.forward(150)         # tell Fahim to move forward by 150 units
    # Fahim.left(90)             # turn by 90 degrees
    # Fahim.forward(75)          # complete the second side of a rectangle

    wn.exitonclick()                # wait for a user click on the canvas



n_S = int(input("Enter the number of squares : "))
pixel= int(input("Enter the lenth in pixel   : "))

square_turtle(n_S,pixel)
