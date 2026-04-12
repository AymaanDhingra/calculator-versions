import math

class ScientificCalculator:
    """Scientific Calculator - Version 4.0"""
    
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
    
    # Scientific operations
    def sine(self, angle_degrees):
        """Calculate sine (angle in degrees)"""
        angle_radians = math.radians(angle_degrees)
        self.result = math.sin(angle_radians)
        self.history.append(f"sin({angle_degrees}°) = {self.result}")
        return self.result
    
    def cosine(self, angle_degrees):
        """Calculate cosine (angle in degrees)"""
        angle_radians = math.radians(angle_degrees)
        self.result = math.cos(angle_radians)
        self.history.append(f"cos({angle_degrees}°) = {self.result}")
        return self.result
    
    def tangent(self, angle_degrees):
        """Calculate tangent (angle in degrees)"""
        angle_radians = math.radians(angle_degrees)
        self.result = math.tan(angle_radians)
        self.history.append(f"tan({angle_degrees}°) = {self.result}")
        return self.result
    
    def logarithm(self, num, base=10):
        """Calculate logarithm"""
        if num <= 0:
            return "Error: Logarithm undefined for non-positive numbers"
        self.result = math.log(num, base)
        self.history.append(f"log({num}) base {base} = {self.result}")
        return self.result
    
    def natural_log(self, num):
        """Calculate natural logarithm (ln)"""
        if num <= 0:
            return "Error: Logarithm undefined for non-positive numbers"
        self.result = math.log(num)
        self.history.append(f"ln({num}) = {self.result}")
        return self.result
    
    def factorial(self, num):
        """Calculate factorial"""
        if num < 0:
            return "Error: Factorial not defined for negative numbers"
        self.result = math.factorial(int(num))
        self.history.append(f"{int(num)}! = {self.result}")
        return self.result
    
    # Memory functions
    def memory_add(self):
        self.memory += self.result
        print(f"Memory: {self.memory}")
    
    def memory_subtract(self):
        self.memory -= self.result
        print(f"Memory: {self.memory}")
    
    def memory_clear(self):
        self.memory = 0
        print("Memory cleared!")
    
    def memory_recall(self):
        self.result = self.memory
        return self.result
    
    def show_history(self):
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
    calc = ScientificCalculator()
    
    print("=" * 50)
    print("SCIENTIFIC CALCULATOR - Version 4.0")
    print("Advanced Mathematical Operations")
    print("=" * 50)
    
    while True:
        print("\n--- Basic Operations ---")
        print("1. Add      2. Subtract  3. Multiply  4. Divide")
        print("5. Power    6. Square Root")
        print("\n--- Trigonometric Functions ---")
        print("7. Sine     8. Cosine    9. Tangent")
        print("\n--- Logarithmic Functions ---")
        print("10. Logarithm (base 10)  11. Natural Log (ln)  12. Factorial")
        print("\n--- Memory Functions ---")
        print("13. M+      14. M-       15. MR       16. MC")
        print("17. Show History   18. Exit")
        
        choice = input("\nEnter choice (1-18): ")
        
        if choice == '18':
            print("Thank you for using the Scientific Calculator!")
            break
        
        try:
            if choice == '1':
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                print(f"Result: {calc.add(num1, num2)}")
            
            elif choice == '2':
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                print(f"Result: {calc.subtract(num1, num2)}")
            
            elif choice == '3':
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                print(f"Result: {calc.multiply(num1, num2)}")
            
            elif choice == '4':
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                result = calc.divide(num1, num2)
                print(f"Result: {result}")
            
            elif choice == '5':
                base = float(input("Enter base: "))
                exponent = float(input("Enter exponent: "))
                print(f"Result: {calc.power(base, exponent)}")
            
            elif choice == '6':
                num = float(input("Enter number: "))
                result = calc.square_root(num)
                print(f"Result: {result}")
            
            elif choice == '7':
                angle = float(input("Enter angle (in degrees): "))
                print(f"Result: {calc.sine(angle)}")
            
            elif choice == '8':
                angle = float(input("Enter angle (in degrees): "))
                print(f"Result: {calc.cosine(angle)}")
            
            elif choice == '9':
                angle = float(input("Enter angle (in degrees): "))
                print(f"Result: {calc.tangent(angle)}")
            
            elif choice == '10':
                num = float(input("Enter number: "))
                result = calc.logarithm(num)
                print(f"Result: {result}")
            
            elif choice == '11':
                num = float(input("Enter number: "))
                result = calc.natural_log(num)
                print(f"Result: {result}")
            
            elif choice == '12':
                num = float(input("Enter number: "))
                result = calc.factorial(num)
                print(f"Result: {result}")
            
            elif choice == '13':
                calc.memory_add()
            
            elif choice == '14':
                calc.memory_subtract()
            
            elif choice == '15':
                print(f"Memory Value: {calc.memory_recall()}")
            
            elif choice == '16':
                calc.memory_clear()
            
            elif choice == '17':
                calc.show_history()
            
            else:
                print("Invalid choice!")
        
        except ValueError:
            print("Invalid input! Please enter valid numbers.")
