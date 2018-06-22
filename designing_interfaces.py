import turtle
import math

refobject = turtle.Turtle()


def square(refrence,length):
    
    for each in range(4):
        refrence.fd(length)
        refrence.lt(90)
    turtle.mainloop()
    
    


def polygon(refrence,length,side):
    for each in range(side):
        refrence.fd(length)
        refrence.lt(360/side)
    turtle.mainloop()


def circle(tortoise,radius):
    polygon(tortoise,(math.pi*2*radius)/360,360)

circle(refobject,100)
