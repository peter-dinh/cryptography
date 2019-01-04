import numpy as np

list_character = []

for i in range(65, 91):
    list_character.append(chr(i))


def decode(character, key):
    if character == " ":
        return " " 
    else:
        index = list_character.index(character)
        index_decode = abs((index - key) % 26) 
        return list_character[index_decode]

def encode(character, key):
    if character == " ":
        print("ok")
        return " "
    else:
        index = list_character.index(character)
        index_encode = abs((index + key) % 26) 
        return list_character[index_encode]

if __name__ == '__main__':
    x = input()
    for item in list(x):
        print(encode(item, 3))
    
    # k = "PHHW"
    # for item in list(k):
    #     print(decode(item,3))
