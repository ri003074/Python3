word = "sample"

print(f'{word[::-1]}')  # elpmas


for char in reversed(word):
    print(char)


print(f'{word[0:3]}')  # sam
print(f'{word[:5]}')  # samp1

word1 = "    smaple  "

word1 = word1.strip()
print(word1)


word2 = '10'.zfill(6)
print(f'{word2}')


print('sample'.find('am', 0, 5))


print('sam' in 'sample')


print("\nisalpha")
print('123'.isalpha())
print('abc'.isalpha())
print('1abc'.isalpha())

print("\nisalnum")
print('abc'.isalnum())
print(''.isalnum())

print("\nisspace")
print(' abc'.isspace())
print(' '.isspace())

print("\nlstrip")
word3 = '   abc   '.lstrip()
print(word3)

print("\nrstrip")
word4 = '   abc   '.rstrip()
print(word4)

print("\njoin")
words = ["this", "is", "a", "pen"]
print(' '.join(words))

print("\nstartwith")
print('sample'.startswith(('sam', 'Sam')))
print('sample'.startswith(('asam', 'Sam')))
