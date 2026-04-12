import math

class CalculatorWithMemory:
    """Calculator with Memory - Version 3.0"""
    
    def __init__(self):
        self.result = 0
        self.memory = 0
        self.history = []
    
    def add(self, a, b):
        self.result = a + b
        self.history.append(f"{a} + {b} = {self.result}")
        return self.result
    
    def subtract(self, a, b):
        self.result = a - b
        self.history.append(f"{a} - {b} = {self.result}")
        return self.result
    
    def multiply(self, a, b):
        self.result = a * b
        self.history.append(f"{a} × {b} = {self.result}")
        return self.result
    
    def divide(self, a, b):
        if b == 0:
            return "Error: Cannot divide by zero"
        self.result = a / b
        self.history.append(f"{a} ÷ {b} = {self.result}")
        return self.result
    
    def power(self, base, exponent):
        self.result = base ** exponent
        self.history.append(f"{base} ^ {exponent} = {self.result}")
        return self.result
    
    def square_root(self, num):
        if num < 0:
            return "Error: Cannot calculate square root of negative number"
        self.result = math.sqrt(num)
        self.history.append(f"√{num} = {self.result}")
        return self.result
    
    # Memory functions
    def memory_add(self):
        """Add current result to memory"""
        self.memory += self.result
        print(f"Memory: {self.memory}")
    
    def memory_subtract(self):
        """Subtract current result from memory"""
        self.memory -= self.result
        print(f"Memory: {self.memory}")
    
    def memory_clear(self):
        """Clear memory"""
        self.memory = 0
        print("Memory cleared!")
    
    def memory_recall(self):
        """Recall memory value"""
        self.result = self.memory
        return self.result
    
    def show_history(self):
        """Show calculation history"""
        if not self.history:
            print("No history available!")
            return
        print("\n--- Calculation History ---")
        for i, calc in enumerate(self.history, 1):
            print(f"{i}. {calc}")
        print("-" * 25)
    
    def get_result(self):
        return self.result


# Main program
if __name__ == "__main__":
    calc = CalculatorWithMemory()
    
    print("=" * 40)
    print("CALCULATOR - Version 3.0")
    print("With Memory and History")
    print("=" * 40)
    
    while True:
        print("\nSelect operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Power (x^y)")
        print("6. Square Root")
        print("7. Memory Add (M+)")
        print("8. Memory Subtract (M-)")
        print("9. Memory Recall (MR)")
        print("10. Memory Clear (MC)")
        print("11. Show History")
        print("12. Exit")
        
        choice = input("Enter choice (1-12): ")
        
        if choice == '12':
            print("Thank you for using the calculator!")
            break
        
        if choice in ('1', '2', '3', '4', '5', '6'):
            try:
                if choice in ('1', '2', '3', '4', '5'):
                    num1 = float(input("Enter first number: "))
                    num2 = float(input("Enter second number: "))
                    
                    if choice == '1':
                        print(f"Result: {calc.add(num1, num2)}")
                    elif choice == '2':
                        print(f"Result: {calc.subtract(num1, num2)}")
                    elif choice == '3':
                        print(f"Result: {calc.multiply(num1, num2)}")
                    elif choice == '4':
                        result = calc.divide(num1, num2)
                        print(f"Result: {result}")
                    elif choice == '5':
                        print(f"Result: {calc.power(num1, num2)}")
                
                elif choice == '6':
                    num = float(input("Enter number: "))
                    result = calc.square_root(num)
                    print(f"Result: {result}")
            except ValueError:
                print("Invalid input!")
        
        elif choice == '7':
            calc.memory_add()
        elif choice == '8':
            calc.memory_subtract()
        elif choice == '9':
            print(f"Memory Value: {calc.memory_recall()}")
        elif choice == '10':
            calc.memory_clear()
        elif choice == '11':
            calc.show_history()
        else:
            print("Invalid choice!")
