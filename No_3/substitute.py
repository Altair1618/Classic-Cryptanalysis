import os

# HE -> TH
# EL -> HE
# HM -> ER
# TH -> AT
# TM -> EV
# QX -> IN
# ET -> HA
# LA -> EL
# AT -> LA
# GS -> IG
# HY -> WH
dict = {
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
    "MV": "_S",
    "QN": "_M",
}

def main():
    s = ""

    with open(os.path.join(os.path.dirname(__file__), "playfair_raw.txt"), "r") as file:
        content = file.read()

        i = 0
        # for i in range(0, len(content), 2):
        while i < len(content):
            if content[i] == "\n":
                s += "\n"
                i += 1
            
            if content[i:i + 2] in dict:
                s += dict[content[i:i + 2]]
            elif content[i + 1] + content[i] in dict:
                s += dict[content[i + 1] + content[i]][::-1]
            else:
                # s += content[i:i + 2]
                s += "__"
            
            i += 2

    with open(os.path.join(os.path.dirname(__file__), "substituted.txt"), "w") as file:
        file.write(s)


if __name__ == "__main__":
    main()
