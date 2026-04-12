class Calculator:
    """Basic Calculator - Version 1.0"""
    
    def __init__(self):
        self.result = 0
    
    def add(self, a, b):
        """Add two numbers"""
        self.result = a + b
        return self.result
    
    def subtract(self, a, b):
        """Subtract two numbers"""
        self.result = a - b
        return self.result
    
    def multiply(self, a, b):
        """Multiply two numbers"""
        self.result = a * b
        return self.result
    
    def divide(self, a, b):
        """Divide two numbers"""
        if b == 0:
            return "Error: Cannot divide by zero"
        self.result = a / b
        return self.result
    
    def get_result(self):
        """Get the last calculation result"""
        return self.result


# Main program
if __name__ == "__main__":
    calc = Calculator()
    
    print("=" * 40)
    print("CALCULATOR - Version 1.0")
    print("Basic Arithmetic Operations")
    print("=" * 40)
    
    while True:
        print("\nSelect operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")
        
        choice = input("Enter choice (1/2/3/4/5): ")
        
        if choice == '5':
            print("Thank you for using the calculator!")
            break
        
        if choice in ('1', '2', '3', '4'):
            try:
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
            except ValueError:
                print("Invalid input! Please enter numbers only.")
        else:
            print("Invalid choice! Please select 1, 2, 3, 4, or 5.")
