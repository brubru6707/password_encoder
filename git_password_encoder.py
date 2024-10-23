
def print_menu():
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")

def encode_password(password):

    encoded_password = ""

    for digit in password:
        password_digit = (int(digit) + 3) % 10
        encoded_password += str(password_digit)

    return encoded_password


def main():
    while True:
        print_menu()
        menu_number = int(input("Please enter an option: "))
        if menu_number == 3:
            break
        if menu_number == 1:
            original_password = input("Please enter your password to encode: ")
            decoded_password = encode_password(original_password)
            print("Your password has been encoded and stored!")
        if menu_number == 2:
            print(f'The encoded password is {decoded_password}, and the original password is {original_password}.')
if __name__ == '__main__':
    main()