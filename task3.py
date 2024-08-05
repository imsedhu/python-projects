# Input: Get the number from the user
num = int(input("Enter a number: "))

# Initialize a variable to store the factorial
factorial = 1

# Check if the number is negative, positive, or zero
if num < 0:
    print("Factorial is not defined for negative numbers.")
elif num == 0:
    print("Factorial of 0 is 1")
else:
    # Calculate the factorial using a for loop
    for i in range(1, num + 1):
        factorial *= i

    # Print the factorial
    print("Factorial of", num, "is", factorial)
