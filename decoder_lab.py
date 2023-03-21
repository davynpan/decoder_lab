def encode(string):         #Code by Davyn Pan
    new_password = ""
    for i in string:
        new_password = new_password + f"{int(i) + 3}"            #adds 3 to every integer in password
    return new_password


def decode(string):
    decoded_password = ""                   #subtracts 3 from all integers of password
    for i in string:
        decoded_password = decoded_password + f"{int(i) - 3}"
    return decoded_password


while True:
    print("""Menu\n
-------------\n
1. Encode\n
2. Decode\n
3. Quit""")

    menu_option = int(input("Please enter an option: "))

    if menu_option == 1:
        orig_password = input("Please enter your password to encode: ")
        encoded_password = encode(orig_password)
        print("Your password has been encoded and stored!")         #stores encoded password as encoded_password

    if menu_option == 2:
        print(f"The encoded password is {encoded_password}, and the original password is {orig_password}.")

    if menu_option == 3:
        exit()