from fractions import Fraction

# Define the terms
terms = [
    Fraction(4, 7),
    Fraction(0),
    Fraction(-8, 9),
    Fraction(-13, 7),
    Fraction(17, 21)
]

# Grouping logic 
group1 = Fraction(4, 7) + Fraction(-13, 7)
print(f"Group 1 (4/7 - 13/7): {group1}")

group2 = Fraction(-8, 9) + Fraction(17, 21)
print(f"Group 2 (-8/9 + 17/21): {group2}")

# Final sum of groups
final_sum = group1 + group2
print(f"Final Sum: {final_sum}")
