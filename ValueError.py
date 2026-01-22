try:
    num = int(input("Enter your number: "))
    print(num)
except ValueError:
    print("Execution: The value is not an integer")

print("I am outside the try block.")