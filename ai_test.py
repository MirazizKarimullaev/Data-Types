user_input = int(input("Enter a number: "))

try:
    # Try converting to integer first
    val = int(user_input)
    print(f"The input is an integer: {val}")
except ValueError:
    try:
        # If integer conversion fails, try converting to float
        val = float(user_input)
        print(f"The input is a float: {val}")
    except ValueError:
        # If both fail, it's a non-numeric string
        print("The input is a string, not a number.")