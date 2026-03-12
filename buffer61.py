class BinaryConverter:
    def __init__(self, number):
        self.number = number
    def to_binary(self):
        num = self.number
        binary = ""

        if num == 0:
            return "0"
        
        while num > 0:
            remainder = num % 2
            binary = str(remainder) + binary
            num = num // 2

        return binary
    
number = int(input("Enter an integer: "))
converter = BinaryConverter(number)
print("Binary value: ", converter.to_binary())