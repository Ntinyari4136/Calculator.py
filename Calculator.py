import streamlit as st
import math

# --- Core Calculator Class ---
class Calculator:
    def __init__(self):
        self.operations = {}
        self.init()

    def init(self):
        self.operations["+"] = self.add
        self.operations["-"] = self.subtract
        self.operations["*"] = self.multiply
        self.operations["/"] = self.divide

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b

    def add_operation(self, symbol, func):
        self.operations[symbol] = func

    def calculate(self, num1, operation_symbol, num2):
        if operation_symbol not in self.operations:
            raise ValueError("Invalid operation.")
        return self.operations[operation_symbol](num1, num2)


# --- Advanced Operations ---
def exponent(base, exponent):
    return base ** exponent

def square_root(number, _=0):
    if number < 0:
        raise ValueError("Cannot take square root of a negative number.")
    return math.sqrt(number)

def logarithm(number, base):
    if number <= 0 or base <= 0 or base == 1:
        raise ValueError("Invalid input for logarithm.")
    return math.log(number, base)


# --- Streamlit App ---
def main():
    st.title("🧮 Simple Streamlit Calculator")
    st.markdown("Perform basic and advanced calculations easily!")

    # Initialize calculator
    calc = Calculator()
    calc.add_operation("^", exponent)
    calc.add_operation("sqrt", square_root)
    calc.add_operation("log", logarithm)

    # Operation selection
    operations = list(calc.operations.keys())
    operation = st.selectbox("Select operation", operations)

    # Input numbers
    num1 = st.number_input("Enter first number:", value=0.0, format="%.4f")

    # Handle sqrt case (only one input)
    if operation == "sqrt":
        num2 = 0
    else:
        num2 = st.number_input("Enter second number:", value=0.0, format="%.4f")

    # Perform calculation
    if st.button("Calculate"):
        try:
            result = calc.calculate(num1, operation, num2)
            st.success(f"✅ Result: {result}")
        except Exception as e:
            st.error(f"Error: {e}")

    st.markdown("---")
    st.caption("Built with ❤️ using Streamlit")


if __name__ == "__main__":
    main()
