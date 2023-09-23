from playfair import *


def main():
    while True:
        print("[E]ncrypt -- [D]ecrypt -- [Q]uit: ", end="")
        choice = input().upper()
        print()

        if choice == "E":
            ...
        elif choice == "D":
            ...
        elif choice == "Q":
            break
        else:
            print("Invalid choice.", end="\n\n")


if __name__ == '__main__':
    # main()
    print(encrypt("tsaamstuulhum", "sadsscatt"))
