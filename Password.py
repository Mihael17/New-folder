import random
import string


def main():
    print("Password Generator")
    
    #try:
        #length = int(
            #input("How long do you want your password to be (minimum of 8 number)"))
                    
    #except:
        #print("Input numbers only")
    #password_length = 0
    #while password_length < length:
        #print("Your password must have at least 8 characters")
    password_length = get_Password_Length()

    all_characters = get_Characters()
    password = generate_Password(all_characters, password_length)
    print("\nYour password is: " + password)
    


def get_Password_Length():
    password_length = int(input("\nHow long do you want your password to be (minimum of 8 number)"))
    while password_length < 8:
            print("Your password must have at least 8 characters\n")
            password_length = int(input("Enter the length of password: "))
    return password_length

     


def get_Characters():
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    num = string.digits


    all_characters = lower + upper + num 
    return all_characters


def generate_Password(all_characters, password_length):
    password = "".join(random.sample(all_characters, password_length))
    return password


main()