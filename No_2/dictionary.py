import os
from utils import dump_file


def search_ngram(text, n):
    lib = dict()

    for i in range (len(text)-n+1):
        substr = text[i:i+n]
        if (substr in lib):
          lib[substr].append(i)
        else:
          lib[substr] = [i]
    
    output_file = "dict/dictionary-"+str(n)+"-gram.txt"
    dump_file(lib,output_file)
      
    
    
def main ():
    with open(os.path.join(os.path.dirname(__file__), "input.txt"), "r") as file:
        content = ''
        for line in file :
           stripped_line = line.replace('\n', '')
           content += stripped_line

    # Sanitize
    content.replace("\n", "")
    for i in range (3,7):
      search_ngram(content, i)


if __name__ == "__main__":
    main()