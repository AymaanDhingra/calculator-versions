import math

class AdvancedCalculator:
    """Advanced Calculator - Version 2.0"""
    
    def __init__(self):
        self.result = 0
    
    def add(self, a, b):
        self.result = a + b
        return self.result
    
    def subtract(self, a, b):
        self.result = a - b
        return self.result
    
    def multiply(self, a, b):
        self.result = a * b
        return self.result
    
    def divide(self, a, b):
        if b == 0:
            return "Error: Cannot divide by zero"
        self.result = a / b
        return self.result
    
    # Advanced operations
    def power(self, base, exponent):
        """Calculate base to the power of exponent"""
        self.result = base ** exponent
        return self.result
    
    def square_root(self, num):
        """Calculate square root"""
        if num < 0:
            return "Error: Cannot calculate square root of negative number"
        self.result = math.sqrt(num)
        return self.result
    
    def percentage(self, num, percent):
        """Calculate percentage"""
        self.result = (num * percent) / 100
        return self.result
    
    def get_result(self):
        return self.result


# Main program
if __name__ == "__main__":
    calc = AdvancedCalculator()
    
    print("=" * 40)
    print("CALCULATOR - Version 2.0")
    print("Advanced Operations")
    print("=" * 40)
    
    while True:
        print("\nSelect operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Power (x^y)")
        print("6. Square Root")
        print("7. Percentage")
        print("8. Exit")
        
        choice = input("Enter choice (1-8): ")
        
        if choice == '8':
            print("Thank you for using the calculator!")
            break
        
        if choice in ('1', '2', '3', '4', '5', '6', '7'):
            try:
                if choice in ('1', '2', '3', '4', '5', '7'):
                    num1 = float(input("Enter first number: "))
                    num2 = float(input("Enter second number: "))
                    
                    if choice == '1':
                        print(f"{num1} + {num2} = {calc.add(num1, num2)}")
                    elif choice == '2':
                        print(f"{num1} - {num2} = {calc.subtract(num1, num2)}")
                    elif choice == '3':
                        print(f"{num1} × {num2} = {calc.multiply(num1, num2)}")
                    elif choice == '4':
                        result = calc.divide(num1, num2)
                        print(f"{num1} ÷ {num2} = {result}")
                    elif choice == '5':
                        print(f"{num1} ^ {num2} = {calc.power(num1, num2)}")
                    elif choice == '7':
                        print(f"{num2}% of {num1} = {calc.percentage(num1, num2)}")
                
                elif choice == '6':
                    num = float(input("Enter number: "))
                    result = calc.square_root(num)
                    print(f"√{num} = {result}")
            except ValueError:
                print("Invalid input! Please enter numbers only.")
        else:
            print("Invalid choice! Please select 1-8.")
