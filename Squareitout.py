start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

squares = [i**2 for i in range(start, end + 1)]

even_squares = [x for x in squares if x % 2 == 0]
odd_squares = [x for x in squares if x % 2 != 0]

print("All squares values: ", squares)
print("Even square values: ", even_squares)
print("Odd square values: ", odd_squares)