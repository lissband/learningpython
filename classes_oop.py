#This lesson is fucking important.
#Take fucking good notes and behave well.
#Contributed by Deniz at 16.34,01.07.2018


class FirstClass:
    def setdata(self,value):
        self.data = value
    def display(self):
        print(self.data)

class SecondClass(FirstClass):
    def display(self):
        print('Current value = %s' %self.data)

class ThirdClass(SecondClass):
    def __init__(self,value):
        self.data = value
    def __add__(self,other):
        return (self.data+other)
    def __str__(self):
        return '[ThirdClass:%s]' % self.data
    def mul(self,other):
        self.data *= other
    
