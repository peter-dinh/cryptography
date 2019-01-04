import math
import random

list_character = []
for i in range(65, 91):
    list_character.append(chr(i))


def get_matrix():
    list_matrix = []
    for key in range(0, len(list_character)):
        list_row = []
        for index in range(0, len(list_character)):
            index_decode = abs((index + key) % 26)
            list_row.append(list_character[index_decode])
        list_matrix.append(list_row)
    return list_matrix

data = get_matrix()
# for key in range(0, len(list_character)):
#     print(data[key])


string = 'ATTACKATDAWN'
key = 'LEMON'


x = 0
index = 0
string_key = ''
while x < len(string):
    string_key = string_key +key[index]
    index = index + 1
    if index == len(key):
        index = 0
    x = x + 1
print("keyword: %s"%string_key)


list_encode = ''
for m in range(0, len(string)):
    index_col = list_character.index(string[m])
    index_row = list_character.index(string_key[m])
    list_encode = list_encode + data[index_col][index_row]

print("encode: %s"%list_encode)
list_decode = ''

for m in range(0, len(list_encode)):
    index_row = list_character.index(string_key[m])
    for n in range(0, len(list_character)):
        if data[n][index_row] == list_encode[m]:
            list_decode = list_decode + list_character[n]

print("decode: %s"%list_decode)