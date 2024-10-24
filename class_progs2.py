user_input=input("Enter a string: ")
count = 1  # Initialize count to 1 to account for the first word
i = 0      # Initialize i
while i < len(user_input):
    if user_input[i] == ' ':
        count += 1
    i += 1
print(count)    
