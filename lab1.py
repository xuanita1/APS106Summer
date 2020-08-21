# APS106 Lab 1 - Drawing Shapes with Turtle
# Student Name: Anita Xu
# PRA Section: 0101


################################################
# Part 1 - Finding Errors and Debugging
################################################

# provide access to the Turtle module
import turtle

# bring the turtle to life and call it alex 
alex = turtle.Turtle()

# tell alex where to go in order to draw a SQUARE

#alex.down()          # make alex lower its tail
#alex.setheading(90)  # make alex face north
#alex.forward(100)   # let it run 100 steps 
#alex.left(90)         # turn 90 degrees to the left
#alex.forward(100)
#alex.left(90)
#alex.forward(100)
#alex.left(90)
#alex.forward(100)
#alex.up()           # make alex lift up its tail

#turtle.done()        # close turtle when done

################################################
# Part 2 - Draw A House

################################################
# modify the above code to tell alex to draw a house

#alex.down()
#alex.setheading(45)
#alex.forward(100*(2**(1/2)))
#alex.left(135)
#alex.forward(100)
#alex.right(135)
#alex.forward(100/(2**(1/2)))
#alex.right(90)
#alex.forward(100/(2**(1/2)))
#alex.right(45)
#alex.forward(100)
#alex.right(90)
#alex.forward(100)
#alex.right(90)
#alex.forward(100)
#alex.right(135)
#alex.forward(100*(2**(1/2)))
#turtle.done()

################################################
# Part 3 - Draw Out Your Name
################################################
# tell alex where to go in order to draw your initials: A X 
alex.down()
alex.goto(30, 100)
alex.goto(60,0)
alex.up()
alex.goto(15, 50)
alex.down()
alex.setheading(0)
alex.forward(30)
alex.up() 
alex.goto(80,0)
alex.down()
alex.goto(120,100)
alex.up()
alex.goto(120,0)
alex.down()
alex.goto(80,100)
turtle.done()
