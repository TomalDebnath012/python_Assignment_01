# Problem 20
# Check whether a number is Positive, Negative, or Zero using ternary.
# Then check if it is Even or Odd using nested if-else.
n=int(input("Enter a number: "))
result="Positive" if n>0 else ("Negative" if n<0 else "Zero")
print(result)
if n!=0:
    if n%2==0:
        print("Even")
    else:
        print("Odd")