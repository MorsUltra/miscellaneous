import turtle
from time import sleep

answer = (input(
    "Do you want a virus or circle?: "))  # You don't need the str() here. Input returns a string by default so you don't need to worry about that
if answer == "circle":
    color = input("Pick a background colour: ")
    color2 = input("Pick a colour for the circle P.S. theres rainbow: ")

    if color2 == "rainbow":
        # here you're going to what to do what you did earlier, where it was just one colour.
        # you spin by 10 degrees each time, so you need to loop 36 times.
        # but to make it a rainbow, you need to just change the colour of the turtle each time you spin.
        # I think the easiest way to do that is just to pick a random colour from the "colours" list
        pass

    # i have to say you're good at making things complicated. Welcome to computer science.
    # Do you get why I'm saying you need to loop 36 times?

    # so there's 36 circles? yup and to make 360 degrees cos it moves 10 degrees each time... quick maths
    # yup exactly
    # if you wanted 10 circles, just spin by 36 degrees each time - turtle.left(36)
    # with me? yep awesome dude
    # check out the "random" thing.
    # It's fairly simple to get your head around
    # so you should be all good to just twiddle with the code you already got to make a rainbow option
    # will do
    # Any other questions penis

    turtle.bgcolor(color)
    turtle.pensize(2)
    turtle.speed(0)
    turtle.hideturtle()

    colours = ["red",
               "magenta",
               "blue",
               "cyan",
               "green",
               "yellow",
               "white"]

    turtle.color("red")

    for spin in range(36):  # you're going to draw a circle 36 times
        turtle.circle(100)  # drawing a circle at that position, with radius 100
        turtle.left(10)  # then just spinning on the spot by 10 degrees
        sleep(1)  # it's just "sleep(seconds), so sleep(1) = wait here for 1 second



else:
    color3 = input("Pick a background colour: ")
    color4 = input("Pick a colour for the virus: ")

    turtle.bgcolor(color3)
    turtle.speed(0)
    turtle.pencolor(color4)
    turtle.penup()
    turtle.goto(0, 200)
    turtle.pendown()
    turtle.hideturtle()

    # it sounds really stupid and the reasons are just as stupid, but it's actually quicker to loop using a "for" loop. I can send you videos of it to you but it gets complicated pretty quick.
    # in conclusion, try and use for loops where possible.

    # so here you know it's going to finish looping where b=200, and each loop does b += 1
    # so the "while True" just translates to "for b in range(200)" and you know a = b*3 (I think, don't quote me on that)

    # alternatively if it makes it easier to understand for you, you can just do "while b != 200:", then you can get rid of the whole "if b == 200: break" bit okay i kind of get it
    # does the code work now?
    # probably?

    a = 0
    b = 0

    while True:
        turtle.forward(a)
        turtle.right(b)
        a += 3
        b += 1
        if b == 200:
            break

# youre editing the virus bit not the circle
# well I'm retarded

turtle.exitonclick()
