# Problem 18
# Determine grade and pass/fail status using if-elif-else.
score=int(input("Enter score (0-100): "))
if score>=90 and score<=100:
    print("Grade: A+")
elif score>=80:
    print("Grade: A")
elif score>=60:
    print("Grade: B")
elif score>=40:
    print("Grade: C")
else:
    print("Grade: F")
if score>=40:
    print("Pass")
else:
    print("Fail")