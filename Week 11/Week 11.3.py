def safe_division():
    try:
        num1 = float(input())
        num2 = float(input())

        result = num1 / num2

        print(result)

    except ZeroDivisionError:
        print("Error: Cannot divide or modulo by zero.")

    except ValueError:
        print("Error: Non-numeric input provided.")

safe_division()
