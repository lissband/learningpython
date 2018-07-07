def gcd(num0,num1):
    if num0>num1:
        divisors = []
        for i in range(1,num1+1):
            if num0 % i ==0 and num1 % i ==0:
                divisors.append(i)
        print(divisors)
        return max(divisors)
    elif num1>num0:
        divisors = []
        for i in range(1,num0+1):
            if num0 % i ==0 and num1 % i==0:
                divisors.append(i)
        print(divisors)
        return max(divisors)
    elif num0 == num1:
        return num0

print(gcd(6,12))