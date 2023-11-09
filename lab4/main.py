# ./
# main.py
from des import get_s_for_j
import json


def main():
    bit_block = input("Enter 48-bit block (empty: random): ")
    j = input("Enter j (0: random): ")
    j = int(j) if j != "" else 0

    print()

    s = get_s_for_j(bit_block, j)
    # print(json.dumps(s, indent=4))
    print("48-bit block: " + " ".join([s["bit_block"][i:i+6] for i in range(0, len(s["bit_block"]), 6)]))
    print("j: " + str(s["j"]))
    print("B: " + s["b"])
    print("S{}(B{})".format(s["j"], s["j"]) + ": " + s["s"])


if __name__ == '__main__':
    main()
