#This is like my fucking newborn.I am feeling alive motherfucker.I AM FEELING ALIVE!
#Contribution 01.07.2018 11:04
#Deniz Surmeli

def summation(arg):
    return_thing = 0 
    for item in arg:
        if isinstance(item,(list,tuple)):
            return_thing += summation(item)
        else:
            try:
                return_thing += item
            except:
                pass 
    return return_thing

cheese = [1,2,[(1,2,3,4),3,55,6],11,22]

print(summation(cheese))
                