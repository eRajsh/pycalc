from PyCalcClass import Calc
from PyCalcClass import ScientificCalc

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = str(input("Enter the calculation operation: "))

calc = ScientificCalc("anyname")

if c == "+":
    calc.add(a, b)

if c == "-":
    calc.sub(a, b)

if c == "*":
    calc.mult(a, b)

if c == "/":
    calc.div(a, b)
