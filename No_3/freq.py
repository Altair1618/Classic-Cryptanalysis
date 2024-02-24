import os


def main():
    dict = {}

    with open(os.path.join(os.path.dirname(__file__), "playfair_raw.txt"), "r") as file:
        content = file.read()
        content = ''.join(e for e in content if e.isalpha())

        length = 2
        for i in range(0, len(content) - length + 1, 2):
            gram = content[i:i + length]

            if gram in dict:
                dict[gram] += 1
            else:
                dict[gram] = 1

    filename = "bigram.txt" if length == 2 else "quadrigram.txt" if length == 4 else None
    
    if filename is None:
        raise Exception("Length must be 2 or 4")
    
    with open(os.path.join(os.path.dirname(__file__), filename), "w") as file:
        sorted_dict = dict.items()
        sorted_dict = sorted(sorted_dict, key=lambda x: x[1], reverse=True)

        for key, value in sorted_dict:
            file.write(f"{key}: {value}\n")


if __name__ == "__main__":
    main()
