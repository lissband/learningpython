temperatures = [10,-20,-289,100]

def c_to_f(c):
    if c < -273.15:
        return 'Temperature does not mean anything.'
    else:
        f = c* 9/5 + 32
        return f

for t in temperatures:
    if t <  -273.15:
        pass
    else:
        with open('temperatures.txt','a') as ff:
            ff.write(str(c_to_f(t)))
            ff.write('\n')
