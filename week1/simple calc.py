num1 = float(input("What is 1st number?"))
operator = input("What is the operation?")
num2 = float(input("What is the 2nd number?"))
match operator:
    case "+":
        print("Result:", num1 + num2)
    case "-":
        print("Result:", num1 - num2)
    case "*":
        print("Result:", num1 * num2)
    case "/":
        if num2 == 0:
            print("Result is undefined")
        else:
            print("Result:", num1 / num2)

    case _:
        print("Invalid operator!")
