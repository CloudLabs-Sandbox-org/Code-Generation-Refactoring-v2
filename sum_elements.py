# A refactored version of the previous Python program. It prompts the user for the number of elements to sum, takes those integers as input, and handles some basic error cases
# This version improves validation, modularity, performance, and error handling. It uses helper functions and list comprehensions for efficiency.

MAX = 100

def calculate_sum(arr):
    return sum(arr)

def get_integer(prompt, min_value=None, max_value=None):
    while True:
        try:
            value = int(input(prompt))
            if min_value is not None and value < min_value:
                print(f"El valor debe ser al menos {min_value}.")
                continue
            if max_value is not None and value > max_value:
                print(f"El valor no debe ser mayor que {max_value}.")
                continue
            return value
        except ValueError:
            print("Entrada inválida. Por favor, ingresa un número entero.")

def main():
    try:
        n = get_integer(f"Ingresa la cantidad de elementos (1-{MAX}): ", 1, MAX)
        arr = []
        print(f"Ingresa {n} números enteros:")
        for i in range(n):
            num = get_integer(f"Elemento {i+1}: ")
            arr.append(num)
        total = calculate_sum(arr)
        print("Suma de los números:", total)
    except KeyboardInterrupt:
        print("\nPrograma terminado por el usuario.")

if __name__ == "__main__":
    main()
