class Calculator:
    def __init__(self, input1, input2):
        self.input1 = input1
        self.input2 = input2

    def adder(self):
        result = self.input1 + self.input2
        return result

    def subtractor(self):
        result = self.input1 - self.input2
        return result

    def multiplier(self):
        result = self.input1 * self.input2
        return result

    def divider(self):
        result = self.input1 / self.input2
        return result

    def clear(self):
        self.input1 = self.input2 = 0 

input1 = int(input("Input the first number: "))
input2 = int(input("Input the second number: "))

calculator = Calculator(input1, input2)

add_result = calculator.adder()
print(str(calculator.input1) + " + " + str(calculator.input2) + " = " + str(add_result))
subtract_result = calculator.subtractor()
print(str(calculator.input2) + " - " + str(calculator.input1) + " = " + str(subtract_result))
multiply_result = calculator.multiplier()
print(str(calculator.input1) + " * " + str(calculator.input2) + " = " + str(multiply_result))
divide_result = calculator.divider()
print(str(calculator.input1) + " / " + str(calculator.input2) + " = " + str(divide_result))
clear_result = calculator.clear()
print("Input 1 after clear(): " + str(calculator.input1))
print("Input 2 after clear(): " + str(calculator.input2))

