def is_equal(number):
    dividers = [i for i in range(1,number) if number % i == 0 ]
    print(dividers)
    if sum(dividers) == number:return True 
    else: return False

threes = [i for i in range(1,101) if i%3 ==0]
print(threes)