import random
import string


def main():
    print("Password Generator\n")
    
    try:
        length = int(
            input("How long do you want your password to be (minimum of 8 number)")
        )
    except:
        print("Input numners only")
    password_length = 0
    while password_length < length:
        print("Your password must have at least 8 characters")
        password_length = getPasswordLength()

    all_characters = getCharacters()
    password = generatePassword(all_characters, password_length)
    print("\nYour password is: " + password)
    


def getPasswordLength():
    password_length = int(input("\nEnter the length of password: "))
    if password_length < 8:
        print("Your password must have at least 8 characters\n")
        password_length = int(input("Enter the length of password: "))
        return password_length
    else:        
        return password_length


def getCharacters():
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    num = string.digits


    all_characters = lower + upper + num 
    return all_characters


def generatePassword(all_characters, password_length):
    password = "".join(random.sample(all_characters, password_length))
    return password


main()