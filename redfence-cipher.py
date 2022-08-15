# For information about redfence cipher visit
# https://www.dcode.fr/redefence-cipher
from itertools import cycle
from pydoc import plain

input_text = list(input('input text: '))

if ' ' in input_text:
    if input('do you want to preserve spaces? [Y/N] ')=='N':
        input_text = [i for i in input_text if i!=' ']

output_text = []
mode = input('do you want to [E]ncrypt or [D]ecrypt the text you just entered? ')
key = input('key (must be in format 012...n): ')
key = [int(i) for i in key]


def first_elements(iterable: list, n: int):
    output = []
    for i in range(n):
        output.append(iterable[i])
    return output


# The letters of input_text have to be appended
# to the lists of rows in the order (where each
# nth number is the index of the list where the
# nth letter of input_text will be appended and
# assuming that only 3 rows are used) 0121...0121
#
# Example:
# 0: E---P---E--
# 1: -X-M-L-T-X-
# 2: --A---E---T
def make_redfence(plain_text: list, key_: list):
    order = list(range(len(key_))) \
            +list(range(len(key_)-2, 0, -1))
    output = [[] for _ in range(max(order)+1)]
    j = 0
    for i in cycle(order):
        output[i].append(plain_text[j])
        j += 1
        if j >= len(plain_text):
            break
    return output


# Defines a function that decypts a cipher text
# given the key by first ordering the rows of
# the redfence and then going through this ordered
# redfence and creating the plain text.
# 
# Example:
# Cipher text: AETEPEXMLTX
# Unordered redfence:
# 0: A---P---L--
# 1: -E-E-E-M-T-
# 2: --T---X---X
# Ordered redfence:
# 0: E---P---E--
# 1: -X-M-L-T-X-
# 2: --A---E---T
# Plain text: EXAMPLETEXT
def get_from_redfence(cipher_text: list, key_: list):
    output = []
    
    order = list(range(len(key_))) \
        +list(range(len(key_)-2, 0, -1))
        
    cipher_text_copy = cipher_text.copy()
    rows = [[] for _ in range(len(key_))]
    lengths = [len(i) for i in make_redfence(cipher_text_copy, key_)]
    for i in key_:
        rows[i] = first_elements(cipher_text_copy, lengths[i])
        for _ in range(lengths[i]):
            cipher_text_copy.pop(0)
            
    for i in cycle(order):
        if len(rows[i]) == 0:
            break
        output.append(rows[i][0])
        rows[i].pop(0)
    return output


if mode == 'E':
    rows = make_redfence(input_text, key)
    rows = [''.join(i) for i in rows]

    # All the rows are added to output_text in the
    # order inputted as key
    for i in key:
        output_text += rows[i]
elif mode == 'D':
    output_text = get_from_redfence(input_text, key)


print(''.join(output_text))