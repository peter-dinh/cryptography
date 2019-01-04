import random


string = 'wearediscoveredsaveyourself'

list_character = []

for i in range(97, 123):
    list_character.append(chr(i))

print(list_character)

list_character_key = []

for i in range(0, len(string)):
    index = random.randint(0,25)
    list_character_key.append(list_character[index])

print(list_character_key)
string_encode = ''
for i in range(0, len(string)):
    index_1 = list_character.index(string[i])
    index_2 = list_character.index(list_character_key[i])
    m = (index_1 + index_2) % 26
    string_encode = string_encode + list_character[m]
print(string_encode)
string_decode = ''
for i in range(0, len(string)):
    index_1 = list_character.index(string_encode[i])
    index_2 = list_character.index(list_character_key[i])
    m = (index_1 - index_2) % 26
    string_decode = string_decode + list_character[m]
print(string_decode)