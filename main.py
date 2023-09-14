from caesar import encrypt_caesar, decrypt_caesar


def main():
    while True:
        print("[E]ncrypt, [D]ecrypt, [Q]uit:", end=" ")
        mode = input().upper()
        print()

        if mode == "E":
            print("Message to encrypt:", end=" ")
            message = input()

            while True:
                try:
                    print("Encryption key:", end=" ")
                    key = int(input())
                    break
                except ValueError:
                    print("Key must be an integer")

            print("Keyword (optional):", end=" ")
            keyword = input()

            try:
                output = encrypt_caesar(message, key, keyword)
            except ValueError as e:
                print("Error:", e)
            else:
                print("Encrypted message:", output["encrypted_message"])
                print("Key:", output["key"])
                print("Keyword:", output["keyword"])
                print("Alphabet:", output["alphabet"])

            print()

        elif mode == "D":
            print("Message to decrypt:", end=" ")
            message = input()

            while True:
                print("Decryption key:", end=" ")

                try:
                    key = int(input())
                    break
                except ValueError:
                    print("Key must be an integer")

            print("Keyword (optional):", end=" ")
            keyword = input()

            try:
                output = decrypt_caesar(message, key, keyword)
            except ValueError as e:
                print("Error:", e)
            else:
                print("Decrypted message:", output["message"])
                print("Key:", output["key"])
                print("Keyword:", output["keyword"])
                # print("Alphabet:", output["alphabet"])

            print()

        elif mode == "Q":
            break

        else:
            print("Unknown mode", end="\n\n")


if __name__ == "__main__":
    main()
