n = int(input("Enter a number: "))
sum_even = 0

for i in range(2, n + 1, 2):
    sum_even += i

print("Sum of even natural numbers up to", n, "is:", sum_even)
