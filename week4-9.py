user_input = int(input("Enter a number: "))
for i in range(1, user_input + 1):
    if bin(i)[-1] == '0':
        print(f"{i} is even")
    else:
        print(f"{i} is odd")
