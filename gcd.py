def compute_gcd(num1,num2):
    # Find out minimum number
    if num2 > num1:
        minNum = num1
    else:
        minNum =  num2
    
    for i in range(1,minNum + 1):
        if (num1 % i == 0) and (num2 % i == 0):
            minNum = i

    print(f"The GCD of {num1} and {num2} is : {minNum}")

compute_gcd(12,17)
compute_gcd(4,6)
compute_gcd(336,360)