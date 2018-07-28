class Calc():
    def __init__(self, name):
        self.name = name

    def add(self, a, b):
        result = a + b
        self.prt(self, ("Result = ", result))

    def sub(self, a, b):
        result = a - b
        self.prt(self, ("Result = ", result))

    def div(self, a, b):
        if (a == 0):
            self.prt(self, "illegal operation, number cannot be zero")
        else:
            result = a / b
            self.prt(self, ("Result = ", result))

    def mult(self, a, b):
        result = a * b
        self.prt(self, ("Result = ", result))

    def prt(self, msg):
        print(msg)


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = str(input("Enter the calculation operation: "))

calc = Calc("anyname")

if c == "+":
    calc.add(a, b)

if c == "-":
    calc.sub(calc)

if c == "*":
    calc.mult(a, b)

if c == "/":
    calc.div(a, b)
