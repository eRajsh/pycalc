class Calc():
    def __init__(self, name):
        self.name = name

    def add(self, a, b):
        result = a + b
        self.prt("Result = " + str(result))

    def sub(self, a, b):
        result = a - b
        self.prt("Result = " + str(result))

    def div(self, a, b):
        if (b == 0):
            self.prt("illegal operation number cannot be zero")
        else:
            result = a / b
            self.prt("Result = " + str(result))

    def mult(self, a, b):
        result = a * b
        self.prt("Result = " + str(result))

    def prt(self, msg):
        print(msg)

class ScientificCalc(Calc):
	def power(self, a):
		result = a*a
		self.prt("Result =" +str(result)) 

def test_func(someStr):
	print(someStr)

