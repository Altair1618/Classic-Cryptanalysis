import os
from utils import dump_file, dump_file_count


def search_ngram(text, n):
    lib = dict()
    count_lib = dict()

    for i in range (len(text)-n+1):
        substr = text[i:i+n]
        if (substr in lib):
          lib[substr].append(i)
          count_lib[substr] +=1
        else:
          lib[substr] = [i]
          count_lib[substr] = 1

    # Reversed Sort
    sorted_count_lib = count_lib.items()
    sorted_count_lib = sorted(sorted_count_lib, key=lambda x: x[1], reverse=True)      
    
    output_file = "dict/dictionary-"+str(n)+"-gram.txt"
    count_output_file = "count/"+str(n)+"-gram.txt"
    dump_file(lib,output_file)
    dump_file_count(sorted_count_lib, count_output_file)
      
    
def main ():
    with open(os.path.join(os.path.dirname(__file__), "input.txt"), "r") as file:
        content = ''
        for line in file :
           stripped_line = line.replace('\n', '')
           content += stripped_line

    # Sanitize
    content.replace("\n", "")
    for i in range (1,7):
      search_ngram(content, i)


if __name__ == "__main__":
    main()