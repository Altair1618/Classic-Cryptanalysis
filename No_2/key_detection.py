import os

LENGTH = 12
BASE_ORD = 65

def search_ngram(text, n):
    count_lib = dict()

    for i in range (len(text)-n+1):
        substr = text[i:i+n]
        if (substr in count_lib):
          count_lib[substr] +=1
        else:
          count_lib[substr] = 1

    # Reversed Sort
    sorted_count_lib = count_lib.items()
    sorted_count_lib = sorted(sorted_count_lib, key=lambda x: x[1], reverse=True)    

    return sorted_count_lib

def most_frequent_char(s):
    # Dictionary to store character frequencies
    char_count = {}
    
    # Count occurrences of each character
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    # Find the character with the maximum frequency
    max_char = None
    max_count = 0
    for char, count in char_count.items():
        if count > max_count:
            max_char = char
            max_count = count
    
    return max_char, max_count

def main():
  # Based on previous process, potential key length = 12
  with open(os.path.join(os.path.dirname(__file__), "input.txt"), "r") as file:
    content = ''
    for line in file :
        stripped_line = line.replace('\n', '')
        content += stripped_line
  
  temp_list = []
  # Split string to 12 length substr
  idx = 0
  while (idx < len(content)):

    if (idx + LENGTH < len(content)):
      temp_list.append(content[idx:idx+LENGTH])
      idx += LENGTH
    else :
      temp_list.append(content[idx:])
      idx = len(content)

  group_list = []
  for i in range(LENGTH):
    substr = ''
    for j in range(len(temp_list)):
       substr += temp_list[j][i]
    group_list.append(substr)

  # For each group, do caesar cipher
  # print("Most frequent char on each group")
  # for group in group_list:
  #   print(group)
  #   monogram = search_ngram(group, 1)
  #   print(monogram[:3])
  
  char_key = 'ETA'
  char_list = ['GPV', 'LPA', 'IRX', 'SHB', 'RGA', 'OXD', 'MBV', 'QAU', 'LWF', 'SBH', 'RGN', 'ZKU']

  # Potential key
  res = ''
  for str in char_list:
    potential_char = (ord(str[0]) - BASE_ORD) - (ord(char_key[0]) - BASE_ORD)
    new_char = chr(potential_char + BASE_ORD)
    res += new_char
  print(res)

    

if __name__ == "__main__":
    main()

'''
Most Char English Words -> E, T, A
Most Frequen Char on Each Group:
1. G, P, V 
2. L, P, A 
3. I, R, X 
4. S, H, B 
5. R, G, A    
6. O, X, D
7. M, B, V
8. Q, A, U
9. L, W, F
10. S, B, H
11. R, G, N
12. Z, K , U
'''