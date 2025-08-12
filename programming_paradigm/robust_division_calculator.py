def safe_divide(numerator, denominator):
    try:

        nume = float(numerator)
        deno = float(denominator)
        result = nume / deno
        print(f"The result of the division is", end="")
        return result
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.)
    except ValueError:
        print("Error: Please enter numeric values only.")
