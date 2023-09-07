# Add 
def Add(n1, n2) :
    return n1 + n2

# Subtract
def Subtract(n1, n2) :
    return n1 - n2

# Multiply 
def Multiply(n1,n2) :
    return n1 * n2

# Divide 
def Divide(n1, n2) :
    return n1 / n2

operation = {
    "+" : Add,
    "-" : Subtract,
    "*" : Multiply,
    "/" : Divide
}

num1 = float(input("What's the first number? "))

for symbol in operation :
    print(symbol)

conti = None
while conti != "y" : 
    operation_symbol = input("Pick an operation from the line above: ").strip()
    num2 = float(input("What's the next number? "))
    cal_function = operation[operation_symbol]
    answer = cal_function(num1, num2)
    conti = input(f"Type 'y' to continue calculation with {answer}, or type 'no' to exit. ").lower()
    num1 = answer



print(f"{num1} {operation_symbol} {num2} = {answer}")
