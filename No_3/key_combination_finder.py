guesses = {
    "HE": "TH",
    "EL": "HE",
    "HM": "ER",
    "TH": "AT",
    "TM": "EV",
    "QX": "IN",
    "ET": "HA",
    "LA": "EL",
    "AT": "LA",
    "GS": "IG",
    "HY": "WH",
}

encrypt_list = {}


keys = [
    ["_", "_", "_", "_", "_"],
    ["_", "_", "_", "_", "_"],
    ["_", "_", "_", "_", "_"],
    ["_", "_", "_", "_", "_"],
    ["_", "_", "_", "_", "_"],
]


count = 0


def output_keys():
    print("Keys: ")
    for i in range(5):
        for j in range(5):
            print(keys[i][j], end=" ")
        print()


def get_key_index(char):
    for i in range(5):
        for j in range(5):
            if keys[i][j] == char:
                return (i, j)


def encrypt(plain_text):
    a = get_key_index(plain_text[0])
    b = get_key_index(plain_text[1])

    if a[0] == b[0]:
        return keys[a[0]][(a[1] + 1) % 5] + keys[b[0]][(b[1] + 1) % 5]
    elif a[1] == b[1]:
        return keys[(a[0] + 1) % 5][a[1]] + keys[(b[0] + 1) % 5][b[1]]
    else:
        return keys[a[0]][b[1]] + keys[b[0]][a[1]]
    

def brute_force_put(guessed_alphabets):
    for lhs, rhs in guesses.items():
        found = False

        for char in lhs:
            if char in guessed_alphabets:
                found = True
                break

        if found:
            continue

        for char in rhs:
            if char in guessed_alphabets:
                found = True
                break

        if found:
            continue
        
        if encrypt(rhs) != lhs:
            return

    if len(guessed_alphabets) == 0:
        global count
        count += 1
        output_keys()
        return


    for i in range(5):
        for j in range(5):
            if keys[i][j] == "_":
                keys[i][j] = guessed_alphabets[0]
                brute_force_put(guessed_alphabets[1:])
                keys[i][j] = "_"


def main():
    guessed_alphabets = []

    for lhs, rhs in guesses.items():
        for i in range(2):
            if lhs[i] not in guessed_alphabets:
                guessed_alphabets.append(lhs[i])
            if rhs[i] not in guessed_alphabets:
                guessed_alphabets.append(rhs[i])

    for i in range(5):
        for j in range(5):
            if keys[i][j] in guessed_alphabets:
                guessed_alphabets.remove(keys[i][j])

    brute_force_put(guessed_alphabets)

    print(f"Total number of keys: {count}")


if __name__ == "__main__":
    main()