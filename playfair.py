
# Liet ke cac ky tu
list_character = []
for i in range(65, 91):
    if chr(i) != 'J':
        list_character.append(chr(i))


# Tao khoa 
key = 'playfairexample'
key = key.upper()
print('Khoa: %s' %key)
list_key = []
for i in range(0, len(key)):
    if key[i] not in list_key:
        list_key.append(key[i])

#print(list_key)

# Tao bang gia tri
list_table = []
count = 0
count_list_char = 0
for i in range(0, 5):
    list_row = []
    for j in range(0,5):
        if count < len(list_key):
            list_row.append(list_key[count])
            list_character.remove(list_key[count])
        else:
            list_row.append(list_character[count_list_char])
            count_list_char = count_list_char + 1
        count = count + 1
    list_table.append(list_row)

# for i in range(0, len(list_table)):
#     print(list_table[i])



string = 'hidethegoldinthetreestump'

#thay the j thanh i de tinh toan
string = string.replace('j', 'i')
#in hoa choi
string = string.upper()
print('Ban ro: %s'% string)

#ham tach 2 ky tu
def get_double_char(string):
    list_tmp = []
    while  len(string) != 0:
        item = ''

        if len(string) == 1:
            item = item + string[0]
            string = string
        else:
            item = item + string[0] + string[1]

        list_tmp.append(item)

        string = string[2:len(string)]
    return list_tmp

#ham lay gia tri dong cua tu trong danh sach 2 ky tu
def get_index_row(char):
    if char == 'J':
        char = 'I'
    for i in range(0, len(list_table)):
        if char in list_table[i]:
            return i
#ham lay gia tri cot cua tu trong danh sach 2 ky tu
def get_index_col(char):
    if char == 'J':
        char = 'I'
    for i in range(0, len(list_table)):
        if char in list_table[i]:
            return list_table[i].index(char)

list_tmp = get_double_char(string)
#print(list_tmp)


# ma hoa

# them X neu 2 ky trung nhau
string_tmp2 = ''
for i in list_tmp:
    if len(i) == 2:
        if i[0] == i[1]:
            string_tmp2 =string_tmp2 + i[0] + 'X' + i[1]
        else:
            string_tmp2 = string_tmp2 + i
    else:
        string_tmp2 = string_tmp2 + i[0]
#print(string_tmp2)

# tach 2 ky tu khi them X
list_tmp3 = get_double_char(string_tmp2)


list_encode = ''
for item in list_tmp3:
    if len(item) == 2:
        row_char_1 = get_index_row(item[0])
        row_char_2 = get_index_row(item[1])
        col_char_1 = get_index_col(item[0])
        col_char_2 = get_index_col(item[1])
        if  row_char_1 == row_char_2:
            if col_char_1 + 1 == 5:
                index_col_1 = 0
            else:
                index_col_1 = col_char_1 + 1

            if col_char_2 + 1 == 5:
                index_col_2 = 0
            else:
                index_col_2 = col_char_2 + 1
            list_encode = list_encode + list_table[row_char_1][index_col_1] + list_table[row_char_2][index_col_2]
        elif col_char_1 == col_char_2:
            if row_char_1 + 1 == 5:
                index_row_1 = 0
            else:
                index_row_1 = row_char_1 + 1

            if row_char_2 + 1 == 5:
                index_row_2 = 0
            else:
                index_row_2 = row_char_2 + 1
            list_encode = list_encode + list_table[index_row_1][col_char_1] + list_table[index_row_2][col_char_2]
        else:
            list_encode = list_encode + list_table[row_char_1][col_char_2] + list_table[row_char_2][col_char_1]
    else:
        list_encode = list_encode + item
#ket qua khi ma hoa

print('Ban ma: %s'% list_encode)


#giai ma 
list_decode = ''
list_tmp_decode = get_double_char(list_encode)

for item in list_tmp_decode:
    if len(item) == 2:
        row_char_1 = get_index_row(item[0])
        row_char_2 = get_index_row(item[1])
        col_char_1 = get_index_col(item[0])
        col_char_2 = get_index_col(item[1])
        if  row_char_1 == row_char_2:
            if col_char_1 - 1 < 0:
                index_col_1 = 4
            else:
                index_col_1 = col_char_1 - 1

            if col_char_2 - 1 < 0:
                index_col_2 = 0
            else:
                index_col_2 = col_char_2 - 1
            list_decode = list_decode + list_table[row_char_1][index_col_1] + list_table[row_char_2][index_col_2]
        elif col_char_1 == col_char_2:
            if row_char_1 - 1 < 0:
                index_row_1 = 0
            else:
                index_row_1 = row_char_1 - 1

            if row_char_2 - 1 < 0:
                index_row_2 = 0
            else:
                index_row_2 = row_char_2 - 1
            list_decode = list_decode + list_table[index_row_1][col_char_1] + list_table[index_row_2][col_char_2]
        else:
            list_decode = list_decode + list_table[row_char_1][col_char_2] + list_table[row_char_2][col_char_1]
    else:
        list_decode = list_decode + item

# loai bo ky tu x neu 2 ky tu trung
i = 0
for item in list_decode:
    if item == 'X':
        if list_decode[i-1] == list_decode[i+1]:
            list_decode = list_decode[0:i] + list_decode[i + 1:len(list_decode)]
            i = i - 1
    i = i + 1

#ket qua giai ma
# neu trong ban ro co ky j. can xem xet nghia cua cau de dua ra ket qua chinh xac
print('Ban giai ma: %s'% list_decode)
