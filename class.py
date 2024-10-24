user_input = input("Enter a string: ")
pallindrome = ''
for i in range(len(user_input) - 1, -1, -1):
    pallindrome += user_input[i]
if user_input == pallindrome:
    print("Pallindrome")
else:
    print("Not a Pallindrome")