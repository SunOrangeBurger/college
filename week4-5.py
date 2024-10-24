user_input=int(input("Enter a number: "))
for i in range(1,user_input+1):
    if i%3==0 and i%5!=0:
        print("Fizz")
    elif i%5==0 and i%3!=0:
        print("Buzz")
    elif i%3==0 and i%5==0:
        print("FizzBuzz")
    else:
        print(i)
