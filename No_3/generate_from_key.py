import os


keys = [
    ["A", "T", "H", "E", "L"],
    ["I", "Z", "Y", "Q", "U"],
    ["G", "C", "K", "D", "O"],
    ["S", "V", "R", "M", "P"],
    ["X", "B", "W", "N", "F"],
]


def main():
    with open(os.path.join(os.path.dirname(__file__), "substitute.txt"), "w") as file:
        for ai in range(5):
            for aj in range(5):
                for bi in range(5):
                    for bj in range(5):
                        if ai == bi and aj == bj:
                            continue

                        if keys[ai][aj] == "_" or keys[bi][bj] == "_":
                            continue

                        if ai == bi:
                            if keys[ai][(aj - 1) % 5] + keys[bi][(bj - 1) % 5] == "__":
                                continue

                            if keys[ai][aj] + keys[bi][bj] != keys[ai][(aj - 1) % 5] + keys[bi][(bj - 1) % 5]:
                                file.write(f"{keys[ai][aj]}{keys[bi][bj]} ")
                                file.write(f"{keys[ai][(aj - 1) % 5]}{keys[bi][(bj - 1) % 5]}\n")
                        elif aj == bj:
                            if keys[(ai - 1) % 5][aj] + keys[(bi - 1) % 5][bj] == "__":
                                continue

                            if keys[ai][aj] + keys[bi][bj] != keys[(ai - 1) % 5][aj] + keys[(bi - 1) % 5][bj]:
                                file.write(f"{keys[ai][aj]}{keys[bi][bj]} ")
                                file.write(f"{keys[(ai - 1) % 5][aj]}{keys[(bi - 1) % 5][bj]}\n")
                        else:
                            if keys[ai][bj] + keys[bi][aj] == "__":
                                continue

                            if keys[ai][aj] + keys[bi][bj] != keys[ai][bj] + keys[bi][aj]:
                                file.write(f"{keys[ai][aj]}{keys[bi][bj]} ")
                                file.write(f"{keys[ai][bj]}{keys[bi][aj]}\n")


if __name__ == "__main__":
    main()
