import random
import string

def generate_password(length):
    characters = string.ascii_lowercase + string.ascii_uppercase + string.digits

    password_list = []
     
    for i in range(length):
       password_list.append(random.choice(characters))

    random.shuffle(password_list)

    password = ''.join(password_list)

    return password

length = int(input("Enter the password length: "))

print("Generated password : ", generate_password(length))