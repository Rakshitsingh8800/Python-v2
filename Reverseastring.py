str = input("Please enter your own String: ")

str2 = ('')
for i in str:
    str2 = i + str2
    print("\nThe original String = ", str)
    print("\nThe Reversed String = ", str2)