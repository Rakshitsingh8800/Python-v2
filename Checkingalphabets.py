ch = input("Enter a character: ")

if ch.isalpha() and len(ch) == 1:
    print("The given character is an alphabet.")
else:
    print("The given character is not an alphabet.")