def check_age():
    while True:
        try:
            # Prompt the user to enter their age
            age_str = input("Please enter your age: ")
            age = int(age_str)

            
            if age <= 0:
                print("Error: Age cannot be zero or negative. Please enter a valid, positive age.")
                continue  

            break

        except ValueError:
            
            print(f"Error: '{age_str}' is not a valid integer. Please enter a whole number for your age.")
            

    if age % 2 == 0:
        parity_message = "even"
    else:
        parity_message = "odd"

    print(f"\nSuccessfully recorded age: {age}")
    print(f"The age {age} is an {parity_message} number.")

# Run the function
check_age()
