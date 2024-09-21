import random
from number_shuffler import numberGenerator

alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
             'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
sp_char = ['!', '#', '$', '%', '&', '*', '+', '/', '<', '>', '?', '@']

# User inputs for password composition
pass_al = int(input("How many alphabets?: "))
pass_num = int(input("How many numbers?: "))
pass_sp = int(input("How many special characters?: "))

# List to store the password
password = []

for i in range(pass_al):
    password.append(random.choice(alphabets))

for i in range(pass_num):
    password.append(random.choice(numbers))

for i in range(pass_sp):
    password.append(random.choice(sp_char))

# un-shuffled password
print("un-shuffled password:", password)

random_numbers = numberGenerator(len(password))  # Pass the length of the password

shuffled_password = [password[i] for i in random_numbers]

# Convert the shuffled list to a string
generated_password = ''.join(shuffled_password)

print("Generated password:", generated_password)
