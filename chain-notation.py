# See https://youtu.be/-vvhwLTuK6M for more information
from string import ascii_lowercase
from random import shuffle

plain_text = list(ascii_lowercase)
cipher_text = plain_text.copy()
shuffle(cipher_text)
print('plain text:  {}'.format(''.join(plain_text)))
print('cipher text: {}'.format(''.join(cipher_text)))

chains = []

while plain_text!=[]:
    chain = []
    next_value = plain_text[0]
    while not next_value in chain:
        chain.append(next_value)
        # Gets the ct character corresponding
        # to the pt character next_value
        next_value = cipher_text[plain_text.index(next_value)]
    chains.append(chain)
    # Removes the elements of chain from the
    # pt so that the algorithm can start again
    # (the first next_value is the first
    # character of the pt)
    for i in chain:
        plain_text.remove(i)
        cipher_text.remove(i)

print('chain:     {}'.format([''.join(i) for i in chains]))