import os

dict = {
    "E": "E",
    "H": "T",
    "Z": "H",
    "B": "R",
    "R": "O",
    "A": "S",
    "V": "P",
    "X": "C",
    "M": "Y",
    "C": "D",
    "W": "L",
    "O": "G",
    "Y": "A",
    "L": "I",
    "F": "N",
    "P": "M",
}


def main():
    s = ""

    with open(os.path.join(os.path.dirname(__file__), "cipher_tunggal_raw.txt"), "r") as file:
        content = file.read()

        for char in content:
            if char == "\n":
                s += "\n"
                continue

            if char in dict:
                s += dict[char]
            else:
                s += "_"

    with open(os.path.join(os.path.dirname(__file__), "substituted.txt"), "w") as file:
        file.write(s)


if __name__ == "__main__":
    main()
