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

#circle(refobject,100)



#Here is the idea of encapsulation:
#Wrapping a piece of code up in a function ----> Assigning yor block of code for a shortcut.


#The Idea Of Generalization
#When you make a function more flexible,like parameters,arguments and stuff it is getting more general.It is called //Generalization

#The Idea of Refactoring
#Arrange your code for usability.


