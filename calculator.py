"""
Calculadora básica en Python con validaciones y buenas prácticas.
"""

import sys

def get_number(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Error: Ingresa un número válido.")

def get_operation():
    operations = {'+': 'suma', '-': 'resta', '*': 'multiplicación', '/': 'división'}
    while True:
        op = input("Elige una operación (+, -, *, /): ").strip()
        if op in operations:
            return op
        else:
            print("Operación no válida. Intenta de nuevo.")

def calculate(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        if b == 0:
            print("Error: No se puede dividir entre cero.")
            return None
        return a / b

def main():
    print("Calculadora Básica")
    args = sys.argv[1:]
    if len(args) == 3:
        try:
            num1 = float(args[0])
            num2 = float(args[1])
            op = args[2]
            if op not in ['+', '-', '*', '/']:
                print("Operación no válida. Usa +, -, * o /.")
                return
        except ValueError:
            print("Error: Los dos primeros argumentos deben ser números.")
            return
        result = calculate(num1, num2, op)
        if result is not None:
            print(f"Resultado: {num1} {op} {num2} = {result}")
    else:
        num1 = get_number("Ingresa el primer número: ")
        num2 = get_number("Ingresa el segundo número: ")
        op = get_operation()
        result = calculate(num1, num2, op)
        if result is not None:
            print(f"Resultado: {num1} {op} {num2} = {result}")

if __name__ == "__main__":
    main()
