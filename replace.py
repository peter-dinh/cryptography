import numpy as np
import random

list_character = []

for i in range(65, 91):
    list_character.append(chr(i))

key = []


index = 0
while index != 26:
    rand = random.randint(-1,25)
    if list_character[rand] not in key:
        key.append(list_character[rand])
        index = index + 1

def encode(string):
    string_encode = ''
    for char in string:
        index = list_character.index(char)
        string_encode = string_encode + key[index]
        #print(key[index])
    return string_encode
def decode(string):
    string_decode = ''
    for char in string:
        index = key.index(char)
        string_decode = string_decode + list_character[index]
        #print(list_character[index])
    return string_decode

print(key)

if __name__ == '__main__':
    string = input("nhap ban ro (Capslock): ")
    string_encode = encode(string)
    print(string_encode)
    string_decode = decode(string_encode)
    print(string_decode)