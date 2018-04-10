
"""Simple Four Function Calculator"""

class Calculator(object):
    
    def __init__(self, numberOne, numberTwo):
        self.numberOne = numberOne
        self.numberTwo = numberTwo

    def add(self):
        answer = self.numberOne + self.numberTwo
        return answer

    def multiply(self):
        answer = self.numberOne * self.numberTwo
        return answer

    def subtract(self):
        answer = self.numberOne - self.numberTwo
        return answer

    def divide(self):
        answer = self.numberOne/self.numberTwo
        return answer

    def intake(self, prompt):
        numOne = input("First Number: ")
        while(not numOne.isdigit()):
            numOne = input("Please insert a number: ")
        if(prompt == 4):
            while(numOne == 0):
                numOne = input("Please insert a number that isn't zero: ")
        self.numberOne = int(numOne)
        numTwo = input("Second Number: ")
        while(not numTwo.isdigit()):
            numTwo = input("Please insert a number: ")
        self.numberTwo = int(numTwo)

    def run(self):
        prompt = 0
        while(prompt != -1):
            print("What would you like to do?\n1. Add\n2. Multiply\n3. Subtract\n4. Divide\n-1. Exit ")
            prompt = int(input())
            if(prompt == 1):
                self.intake(1)
                print(self.add()),
            elif(prompt == 2):
                self.intake(2)
                print(self.multiply()),
            elif(prompt == 3):
                self.intake(3)
                print(self.subtract()),
            elif(prompt == 4):
                self.intake(4)
                print(self.divide()),
            elif(prompt == -1):
                print("Have a good day!\n")
            else:
                print("That is not a choice\n")
                


cal = Calculator(0, 0)
cal.run()

            
