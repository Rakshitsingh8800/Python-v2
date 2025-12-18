age = int(input("Enter your age: "))

if age >= 0 and age <= 10:
    print("You are a Child.")
elif age >= 11 and age <= 17:
    print("You are a Teenager.")
elif age >= 18:
    print("You are an Adult.")
else:
    print("Invalid age entered.")
