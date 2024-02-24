import os


with open(os.path.join(os.path.dirname(__file__), "substitute.txt"), "r") as file:
    lines = file.readlines()
    
    for line in lines:
        without_newline = line.strip()
        splitted = without_newline.split(" ")
        print(f"\"{splitted[0]}\": \"{splitted[1]}\",")
