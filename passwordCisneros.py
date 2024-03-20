def main():  # Jose Cisneros
    menuOption = 0
    while menuOption != 3:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        menuOption = int(input("Please enter an option: "))
        if menuOption == 1:
            encodedPassword = encode()
        if menuOption == 2:
            decode(encodedPassword)
        if menuOption == 3:
            exit()
        elif menuOption <= 0 or menuOption > 3:
            errorPath()


def errorPath():  # Jose Cisneros
    print("The choice you selected was incorrect! Please enter a correct number!\n")
    main()


def encode():  # Jose Cisneros
    decodedPassword = (input("Please enter a password to encode: "))
    password = ''
    for num in decodedPassword:
        num = int(num)
        num += 3
        if num >= 10:
            num -= 10
        password = password + str(num)
    print("Your password has been encoded and stored!\n")
    return password


def decode(encodedPassword):  # Nathan McTear
    decodedPassword = ''
    for num in encodedPassword:
        num = int(num)
        num -= 3
        if num < 0:
            num += 10
        decodedPassword += str(num)
    print(f'The encoded password is {encodedPassword}, and the original password is {decodedPassword}.')


if __name__ == '__main__':
    main()