i=0
sum=0
num=int(input("Enter a number: "))
str_num=str(num)
leng=len(str_num)
while True:
    sum=sum+num//(10**i)%10
    i+=1
    if i==leng:
        break
print(sum)
