#!/usr/bin/env python3
"""
Simple CLI Calculator
Version: 2.0.0
"""

VERSION = "2.0.0"


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b


def power(a, b):
    return a ** b


def modulus(a, b):
    return a % b


MENU = """
==============================
   Simple Calculator v{}
==============================
1. Add        (+)
2. Subtract   (-)
3. Multiply   (*)
4. Divide     (/)
5. Power      (^)
6. Modulus    (%)
7. Exit
==============================
"""


def get_operation_choice():
    return input("Select operation (1-7): ").strip()


def get_float(prompt):
    """Keep asking until the user provides a valid number. Fixes BUG-02 (v1.0.0 crash on
    non-numeric input)."""
    while True:
        raw = input(prompt).strip()
        try:
            return float(raw)
        except ValueError:
            print("Error: Please enter a valid number.")


def get_numbers():
    a = get_float("Enter first number: ")
    b = get_float("Enter second number: ")
    return a, b


def run():
    while True:
        print(MENU.format(VERSION))
        choice = get_operation_choice()

        if choice == "7":
            print("Goodbye!")
            break

        if choice not in {"1", "2", "3", "4", "5", "6"}:
            print("Invalid choice. Please select 1-7.")
            continue

        a, b = get_numbers()

        try:
            if choice == "1":
                result = add(a, b)
            elif choice == "2":
                result = subtract(a, b)
            elif choice == "3":
                result = multiply(a, b)
            elif choice == "4":
                result = divide(a, b)
            elif choice == "5":
                result = power(a, b)
            elif choice == "6":
                result = modulus(a, b)
        except ZeroDivisionError as e:
            # Fixes BUG-01 (v1.0.0 crash on divide-by-zero)
            print(f"Error: {e}")
            continue

        print(f"Result: {result}")


if __name__ == "__main__":
    run()
