def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def main(): 
    print("Simple Calculator")
    print("Type 'exit' to quit the calculator")
    while True:
        print("\nAvailable operations: +, -, *, /")
        first_input = input("Enter first number (or 'exit' to quit): ")
        
        if first_input.lower() == 'exit':
            print("Thank you for using the calculator!")
            break
            
        try:
            num1 = float(first_input)
            op = input("Enter operation (+, -, *, /): ")
            num2 = float(input("Enter second number: "))
            
            if op == '+':
                result = add(num1, num2)
            elif op == '-':
                result = subtract(num1, num2)
            elif op == '*':
                result = multiply(num1, num2)
            elif op == '/':
                result = divide(num1, num2)
            else:
                result = "Invalid operation"
                
            print("Result:", result)
        except ValueError as e:
            print("Error:", str(e))
        except Exception as e:
            print("An error occurred:", str(e))
    
if __name__ == "__main__":
    main()
