class simpleCalculator():
    
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2
    
    def addition(self):
        total = self.num1 +  self.num2
        print(f"The addition of {self.num1} and {self.num2} is {total}")
        return total
    
    def substraction(self):
        total = self.num1 -  self.num2
        print(f"The substraction of {self.num1} and {self.num2} is {total}")
        return total
    
    def multiplication(self):
        total = self.num1 *  self.num2
        print(f"The multiplication of {self.num1} and {self.num2} is {total}")
        return total
    
    def division(self):
        total = self.num1 /  self.num2
        print(f"The division of {self.num1} and {self.num2} is {total}")
        return total
    
    def driver_code(self):
        print("Welcome to mini calculator!!!")

        choices = {
            "1": "Addition",
            "2": "Substraction",
            "3": "Multiplication",
            "4": "Division",
            "5": "Exit",
        }

        for i in choices.keys():
            print(f"{i} --> {choices[i]}")

        user_ip = input("Please choose one of calculator function!")
        user_value =choices.get(user_ip,-1)
    
        if user_value == -1:
            print("Wrong choice Please Try again!")
        if user_value == "Addition":
            self.num1 = int(input("Please Enter the num1 value : "))or self.num1
            self.num2 = int(input("Please Enter the num2 value : ") )or self.num2
            simpleCalculator(self.num1,self.num2).addition()
        if user_value == "Substraction":
            self.num1 = int(input("Please Enter the num1 value : "))or self.num1
            self.num2 = int(input("Please Enter the num2 value : ") )or self.num2
            simpleCalculator(self.num1,self.num2).substraction()
        if user_value == "Multiplication":
            self.num1 = int(input("Please Enter the num1 value : "))or self.num1
            self.num2 = int(input("Please Enter the num2 value : ") )or self.num2
            simpleCalculator(self.num1,self.num2).multiplication()
        if user_value == "Division":
            self.num1 = int(input("Please Enter the num1 value : "))or self.num1
            self.num2 = int(input("Please Enter the num2 value : ") )or self.num2
            simpleCalculator(self.num1,self.num2).division()
        if user_value == "Exit":
            print("Thank you!")

        while input("Do You Want To Continue? [y/n]: ") == "y":
            simpleCalculator.driver_code(self)

si = simpleCalculator(10,20)
si.driver_code()