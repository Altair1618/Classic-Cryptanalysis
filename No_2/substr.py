from utils import dump_file, read_file
  

def search_repeated_substr(lib: dict):
  new_lib = dict()
  for key in lib:
    current_val = lib[key]

    if (len(current_val) > 1):
      temp = []
      for i in range(len(current_val) -1):
        temp.append(int(current_val[i+1]) - int(current_val[i]))
      
      new_lib[key] = temp
  
  return new_lib

def main():
  for i in range (3,7):
    input_file = "dict/dictionary-"+str(i)+"-gram.txt"
    lib = read_file(input_file)

    new_lib = search_repeated_substr(lib)
    output_file = 'substr/range-repeated-'+str(i)+'-gram.txt'
    dump_file(new_lib, output_file)

if __name__ == "__main__":
    main()