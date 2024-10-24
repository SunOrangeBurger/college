n=10
while n>=0:
    if n%2==0 and n!=0:
        print("even:",n)
        n=n-1
    elif n%2!=0:
        print("odd:",n)
        n=n-1
    elif n==0:
        print("blastoff")
        break

