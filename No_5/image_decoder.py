import math


def affine_decipher(hex_values, inv_m, b, n):
    decipher_hex = []
    for hex_value in hex_values:
        C = hex((inv_m * (int(hex_value, 16) - b)) % n)
        decipher_hex.append(C)
    return decipher_hex


def read_image_to_hex(image_path):
    try:
        with open(image_path, "rb") as image:
            f = image.read()
            b = bytearray(f)
            array_of_hex = [hex(byte) for byte in b]
            return array_of_hex
    except FileNotFoundError:
        print("Error: File not found.")
        return None
    except ValueError as e:
        print("Error:", e)
        return None
    

def array_of_hex_to_bytearray(array_of_hex):
    bytearray_data = bytearray()
    for hex_value in array_of_hex:
        if hex_value.startswith('0x'):
            hex_value = hex_value[2:]
        byte_value = int(hex_value, 16)
        bytearray_data.append(byte_value)
    return bytearray_data


def create_file_from_bytes(file_path, bytes_data):
    try:
        with open(file_path, "wb") as file:
            file.write(bytes_data)
            print("File berhasil dibuat:", file_path)
    except Exception as e:
        print("Error:", e)


def main():
    image_path = "./chall.jpg"
    hex_values = read_image_to_hex(image_path)

    if hex_values is not None:
        deciphered_hex = affine_decipher(hex_values, 137, 201, 256)
        bytearray_cipher = array_of_hex_to_bytearray(deciphered_hex)
        create_file_from_bytes("./deciphered_image.jpg", bytearray_cipher)


if __name__ == "__main__":
    main()