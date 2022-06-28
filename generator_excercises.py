# Generator Exercises

# Problem 1
# Create a generator, primes_gen that generates prime numbers starting from 2.

def primes_gen():
    bases = [2, 3, 5, 7]
    n = 2
    while True:
        if n in bases:
            yield n
        elif True not in [True for base in bases if n % base == 0]:
            yield n
        n += 1


gen = primes_gen()
for _ in range(100):
    print(next(gen), end=' ')


# Expected output
# 2 3 5 7 11 13 17 19 23 29

# ----------------------------------------------------------------------------

# Problem 2
# Create a generator, unique_letters that generates unique letters from
# the input string. It should generate the letters in the same order as
# from the input string.
def unique_letters(text):
    char_list = []
    for character in text:
        if character not in char_list:
            char_list.append(character)
            yield character


for letter in unique_letters('hello'):
    print(letter, end=' ')
# Expected output
# h e l o
