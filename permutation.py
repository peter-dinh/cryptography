
import math
import random


col = 8

string="dinhquangtruonghomquataonhomayday"
count_row = math.ceil(len(string)/col)




print (count_row)

key = []
for i in range(0,8):
    while True:
        number = random.randint(0,7)
        if number not in key:
            key.append(number)
            break
print (key)

def encode(string):
    index = 0
    j = 0
    row = 0
    while  index != len(string):
        matrix[row][j] = string[index]
        j = j + 1
        if j == col:
            j = 0
            row = row + 1
        index = index + 1

    for x in range(0, count_row):
        print(matrix[x])
        #print("\n")

    stt = 0
    string_encode = ''
    while stt != col:
        j = key.index(stt)
        for i in range(0, count_row):
            index 
            if matrix[i][j] != 0:
                string_encode = string_encode + matrix[i][j]
        stt = stt + 1
    print (string_encode)
    return string_encode

list_tmp = [count_row - 1 for i in range(0, col)]

def decode(string):
    index = 0
    i = 0
    j = 0
    mod = len(string) % col
    while index != len(string):
        if mod == 0:
            matrix[i][j] = string[index]
            i = i + 1
            if i == count_row:
                i = 0
                j = j + 1
        else:
            dem = 0
            stt = 0
            while dem != mod:
                m = key[stt]
                list_tmp[m] = count_row
                dem = dem + 1
                stt = stt + 1


            matrix[i][j] = string[index]
            i = i + 1
            if i == list_tmp[j]:
                i = 0
                j = j + 1
        index = index + 1

    for x in range(0, count_row):
        print(matrix[x])
        #print("\n")
    string_decode = ''
    for i in range(0, count_row):
        for item in key:
            if matrix[i][item] != 0:
                string_decode = string_decode + matrix[i][item]
    print(string_decode)
    return string_decode

    
matrix = [[0 for x in range(col)] for y in range(count_row)]
string_encode = encode(string)
matrix = [[0 for x in range(col)] for y in range(count_row)]
decode(string_encode)
