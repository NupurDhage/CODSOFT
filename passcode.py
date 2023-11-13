import string
import random

def passcode_generator(length):
    characters = string.ascii_letters + string.digits
    passcode = ''.join(random.choice(characters) for i in range(length))
    return passcode

if __name__ == "__main__":
    try:
        length = int(input("Enter the length of the passcode: "))
        if length <= 0:
            print("Invalid length! Length should be greater than 0.")
        else:
            print("Your passcode is:", passcode_generator(length))
    except ValueError:
        print("Invalid input! Please enter a valid number.")
