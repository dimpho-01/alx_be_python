def safe_divide(numerator, denominator):
    try:
        answer = float(numerator)/float(denominator)
        result = f"The result of the division is {answer}"
    except ZeroDivisionError:
        result = f"Error: Cannot divide by zero."
    except ValueError:
        result = f"Error: Please enter numeric values only."

    return result