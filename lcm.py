import math
def compute_lcm(num1,num2):
    # find out maximum number
    maxNum = max(num1,num2)

    while True:

        if (maxNum % num1 == 0) and (maxNum % num2 == 0):
            lcm = maxNum
            break 
        maxNum += 1

    print(f"The LCM of {num1} and {num2} is: {lcm} ")


compute_lcm(15,17)
compute_lcm(4,6)