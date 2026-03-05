class PasswordChecker:

    def __init__(self, password):
        self.password = password
    def check_strength(self):
        length = len(self.password)
        has_upper = any(c.isupper() for c in self.password)
        has_lower = any(c.islower() for c in self.password)
        has_digit = any(c.isdigit() for c in self.password)
        has_special = any(not c.isalnum() for c in self.password)

        score = sum ([has_upper, has_lower, has_digit, has_special])

        if length < 6:
            return "Weak Password"
        elif score <= 2:
            return "Medium Password"
        else:
            return "Strong Password"
        
Password = input("Enter password: ")
checker = PasswordChecker(Password)
print("Strength: ", checker.check_strength())