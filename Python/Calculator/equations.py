def userNumbers():
    number1 = input("Input your first number: ")
    number2 = input("Input your second number: ")
    numberList = [number1, number2]
    return numberList

def addition(number1, number2):
    solution = int(number1) + int(number2)
    print(solution)

def subtraction(number1, number2):
    solution = int(number1) - int(number2)
    print(solution)

def multiply(number1, number2):
    solution = int(number1) * int(number2)
    print(solution)

def divide(number1, number2):
    if number2 == 0:
        print("ERROR: Divided by 0\n")
        return
    else:
        solution = float(number1) / float(number2)
        print(solution)
