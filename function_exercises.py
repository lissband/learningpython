#You have made an incredible job Deniz.//Author: Deniz Surmeli P.S:I hope no one see it because it is a hella fucked piece of code...
def do_twice(f,x):
    if f == print:
        f(x,end = '')
        f(x,end= '')
    else:
        f(x)
        f(x)
def do_four(function,argument):
    do_twice(function,argument)
    do_twice(function,argument)

def left_piece(positional):
    print('+',end = '')
    do_four(print,'-')

def under_piece(positional):
    print('|',' '*2,'|',' '*2,'|')
do_twice(left_piece,None)
print('+')
do_four(under_piece,None)
do_twice(left_piece,None)
print('+')
do_four(under_piece,None)
do_twice(left_piece,None)
print('+')