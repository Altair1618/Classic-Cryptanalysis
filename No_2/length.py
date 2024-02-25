from utils import dump_file, read_file
from math import gcd

THRESHOLD = 30

def filter_lib(lib):
  new_lib = dict()
  for key in lib:
     if (lib[key] >= THRESHOLD):
        new_lib[key] = lib[key]

  return new_lib

def solve_gcd(nums):
  if len(nums) == 1:
    return nums[0]

  div = gcd(nums[0], nums[1])

  if len(nums) == 2:
    return div

  for i in range(1, len(nums) - 1):
    div = gcd(div, nums[i + 1])
    if div == 1:
        return div
  return div


def main():
  range_lib = dict()
  for i in range (3,7):
    input_file = "substr/range-repeated-"+str(i)+"-gram.txt"
    lib = read_file(input_file)

    for key in lib:
       for each_val in lib[key]:
          if (each_val in range_lib):
             range_lib[each_val] +=1 
          else:
             range_lib[each_val] =1 
  
  new_lib = filter_lib(range_lib)
  # dump_file(new_lib, "range_counter.txt")
  
  temp_list = []
  for key in new_lib:
     temp_list.append(int(key))

  gcd = solve_gcd(temp_list)
  print("Potential Key Length:", gcd)

if __name__ == "__main__":
    main()