import os

def dump_file(dictionary, filename):
  with open(os.path.join(os.path.dirname(__file__), filename), "w") as convert_file: 
    for key in dictionary:
      convert_file.write(f"{key}: {dictionary[key]}\n")

def read_file(filename):
  lib = dict()
  with open(os.path.join(os.path.dirname(__file__), filename), "r") as file:
    for line in file :
      temp_list = line.split(":")
      val = temp_list[1].replace(" ", "").replace("[","").replace("]","").replace("\n", "").split(",")  
      key = temp_list[0]
      lib[key] = val
  return lib