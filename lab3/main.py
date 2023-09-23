from playfair import *


def main():
    while True:
        print("[E]ncrypt -- [D]ecrypt -- [Q]uit: ", end="")
        choice = input().upper()
        print()

        if choice == "E":
            message = input("Enter the message: ")
            keyword = input("Enter the keyword: ")
            print()

            try:
                result = encrypt(message, keyword)
            except ValueError as error:
                print(error, end="\n\n")
                continue

            print("Message: {}".format(result["message"]))
            print("Ciphertext: {}".format(result["ciphertext"]))
            print("Keyword: {}".format(result["keyword"]))
            print("Encryption text: {}".format(result["encryption_text"]), end="\n\n")
        elif choice == "D":
            ciphertext = input("Enter the ciphertext: ")
            keyword = input("Enter the keyword: ")
            print()

            try:
                result = decrypt(ciphertext, keyword)
            except ValueError as error:
                print(error, end="\n\n")
                continue

            print("Ciphertext: {}".format(result["ciphertext"]))
            print("Message: {}".format(result["message"]))
            print("Keyword: {}".format(result["keyword"]))
            print("Encryption text: {}".format(result["encryption_text"]), end="\n\n")
        elif choice == "Q":
            break
        else:
            print("Invalid choice.", end="\n\n")
            continue


if __name__ == '__main__':
    main()
