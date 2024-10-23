
def print_menu():
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")
    print()

def encode_password(password):

    encoded_password = ""

    for digit in password:
        password_digit = (int(digit) + 3) % 10
        encoded_password += str(password_digit)

    return encoded_password

def decode_password(encoded_password):
    decoded_password = ""
    for digit in encoded_password: 
        encoded_password_digit = (int(digit) - 3) if (int(digit) > 3) else (int(digit) + 7)
        decoded_password += str(encoded_password_digit)

    return decoded_password

def main():
    encoded_password = ""
    while True:
        print_menu()
        menu_number = int(input("Please enter an option: "))
        if menu_number == 3:
            break
        if menu_number == 1:
            original_password = input("Please enter your password to encode: ")
            encoded_password = encode_password(original_password)
            print("Your password has been encoded and stored!\n")
        if menu_number == 2:
            decoded_password = decode_password(encoded_password)
            print(f'The encoded password is {encoded_password}, and the original password is {decoded_password}.\n')
if __name__ == '__main__':
    main()