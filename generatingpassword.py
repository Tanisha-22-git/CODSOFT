print("_____________Password Generator___________")
import random 
def generate_password(length):
    characters_value='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()'
    password = ''.join(random.choice(characters_value) for _ in range(length))
    return password
length = int(input("Please enter the desired length of the Password !"))
password=generate_password(length)
print("The Generated Password as per your desired length is : ",password)
print("------THANK YOU------")