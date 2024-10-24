total_score=0
sub_count=0
while sub_count<5:
    score=int(input(f"Enter a score in subject{sub_count+1}: "))
    if score<0 or score>100:
        print("Invalid score")
        continue
    if score>=90:
        print(f"Subject {sub_count+1} is A")
    elif score>=80:
        print(f"Subject {sub_count+1} is B")
    elif score>=70:
        print(f"Subject {sub_count+1} is C")
    elif score>=60:
        print(f"Subject {sub_count+1} is D")
    else:
        print(f"Subject {sub_count+1} is F")
    total_score+=score
    sub_count+=1
avg_score=total_score/5
print(f"The average score is {avg_score}")
if avg_score >= 90:
    print("The average grade is A")
elif avg_score >= 80:
    print("The average grade is B")
elif avg_score >= 70:
    print("The average grade is C")
elif avg_score >= 60:
    print("The average grade is D")
else:
    print("The average grade is F")
