# main.py

def remainder(a, b):
    if b == 0:
        raise ValueError("Division by zero is not allowed.")
    return a % b
