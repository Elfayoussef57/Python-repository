def calculatrice(a, op, b):
    match op:
        case "+":
            print(a + b)
        case "-":
            print(a - b)
        case "*":
            print(a * b)
        case "/":
            if b == 0:
                raise ZeroDivisionError("Division par zéro")
            print(a / b)
        case _:
            print("Opérateur invalide")

def main():
    while True:
        operation = input("Enter the operation to perform with the form of 'a op b': ")
        if not operation.split(" ", 2):
            print("Invalid operation")
            continue
        a, op, b = operation.split(" ", 2)
        calculatrice(float(a), op, float(b))
        if input("Do you want to continue? (y/n) ") != "y":
            break

if __name__ == "__main__":
    main()
        