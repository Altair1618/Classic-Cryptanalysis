import os
import numpy as np

MODULUS = 26
BASE_ORD = 65
START_TEXT = "Hello Ai Habara"
END_TEXT = "Conan"

def adjugate_matrix(matrix):
    a, b, c = matrix[0]
    d, e, f = matrix[1]
    g, h, i = matrix[2]

    # Calculate the cofactor matrix
    cofactors = np.array([[e*i - f*h, -(b*i - c*h), b*f - c*e],
                          [-(d*i - f*g), a*i - c*g, -(a*f - c*d)],
                          [d*h - e*g, -(a*h - b*g), a*e - b*d]])

    # Transpose the cofactor matrix to get the adjugate matrix
    adjugate = cofactors
    return adjugate

def get_inverse(matrix):
  determinant = np.linalg.det(matrix)
  det_inv = pow(int(determinant), -1, MODULUS)

  adjugate = adjugate_matrix(matrix)
  inv_matrix = (det_inv * adjugate) % MODULUS

  return inv_matrix

def get_key(c_matrix, p_matrix):
  p_matrix = np.transpose(np.array(p_matrix))
  c_matrix = np.transpose(np.array(c_matrix))
  inv_p_matrix = get_inverse(p_matrix)
  result = np.dot(c_matrix, inv_p_matrix) % MODULUS
  return result

def tri_to_num(str):
  temp = []
  for i in str:
    num = ord(i) - BASE_ORD
    temp.append(num)

  temp = np.array(temp)
  return temp    

def split_into_groups_of_three(text):
    if len(text) % 3 == 0:
        groups = [text[i:i+3] for i in range(0, len(text), 3)]
        return groups
    else:
        return "Length of the string is not divisible by 3."

def main():
  with open(os.path.join(os.path.dirname(__file__), "input.txt"), "r") as file:
    content = ''
    for line in file :
        stripped_line = line.replace('\n', '')
        content += stripped_line

  start_text = START_TEXT.upper().replace(" ", "")
  end_text = END_TEXT.upper().replace(" ", "")

  groups_of_three_cipher = split_into_groups_of_three(content)
  list_of_three_cipher = []
  for tri in groups_of_three_cipher:
    temp = tri_to_num(tri)
    list_of_three_cipher.append(temp)
  first_three_cipher = list_of_three_cipher[:3]


  first_nine = start_text[:9]
  first_three_group_cipher = split_into_groups_of_three(first_nine)
  first_three_plain = []
  for tri in first_three_group_cipher:
    temp = tri_to_num(tri)
    first_three_plain.append(temp)

  key = get_key(first_three_cipher, first_three_plain)
  print("Get Key: ")
  print(key)
     

if __name__ == "__main__":
  main()