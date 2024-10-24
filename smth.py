n = int(input("Enter a number to find its factorial: "))
factorial = 1

if n < 0:
    print("Factorial does not exist for negative numbers.")
elif n == 0:
    print("The factorial of 0 is 1.")
else:
    for i in range(1, n + 1):
        factorial *= i
    print(f"The factorial of {n} is {factorial}.")
