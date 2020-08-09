from algorithms.number_theory.euclid import euclid, modinv
import numpy as np
from collections import defaultdict, Counter
from itertools import combinations


def treat_string(s) -> str:
    """
    Treat string to work in lower case and no space
    """
    if not s:
        raise Exception('string is empty')
    s = str.lower(s)
    s = s.replace(' ', '')
    s = s.replace('\n', '')
    s = s.replace(',', '')
    s = s.replace('.', '')

    return s


def factors(n):
    return set(
        factor for i in range(1, int(n ** 0.5) + 1) if n % i == 0
        for factor in (i, n // i)
    )


def string_with_interval(s: str, n: int, start_from=0) -> str:
    a = ''
    for i in range(start_from, len(s), n):
        a += s[i]
    return a


def frequency_analysis(s: str) -> Counter:
    counter = Counter(s)

    return counter


def encrypt_character_shift_cipher(c, a) -> chr:
    c = treat_string(c)

    return chr((((ord(c) - ord('a')) + a) % 26) + ord('a'))


def decrypt_character_shift_cipher(c, a) -> chr:
    c = treat_string(c)

    return chr((((ord(c) - ord('a')) - a) % 26) + ord('a'))


def decrypt_brute_shift_cipher(ciphertext: str):
    """
    Prints all possible alphabetical texts
    """
    ciphertext = treat_string(ciphertext)

    for i in range(26):
        for c in ciphertext:
            print(chr(97 + (ord(c) + i - 97) % 26), end='')
        print('')


def encrypt_affine_cipher(ciphertext: str, a: int, b: int) -> str:
    ciphertext = treat_string(ciphertext)

    if euclid(a, b) != 1:
        raise Exception('keys are not coprime')

    return ''.join([chr(((a * (ord(c) - ord('a')) + b) % 26) + ord('a')) for c in ciphertext])


def decrypt_affine_cipher(ciphertext: str, a: int, b: int) -> str:
    ciphertext = treat_string(ciphertext)

    def decrypt(c):
        x = ord(c) - ord('a')
        decryption = (modinv(a, 26) * (x - b)) % 26
        return chr(decryption + ord('a'))

    return ''.join(map(decrypt, ciphertext))


def decrypt_vigenere_cipher(plaintext: str, key: str) -> str:
    plaintext = treat_string(plaintext)

    key = key * (len(plaintext) // len(key) + 1)
    key = key[:len(plaintext)]
    return ''.join(
        [decrypt_character_shift_cipher(plaintext[i], ord(key[i]) - ord('a')) for i in range(len(plaintext))])


def encrypt_vigenere_cipher(plaintext: str, key: str) -> str:
    plaintext = treat_string(plaintext)

    key = key * (len(plaintext) // len(key) + 1)
    key = key[:len(plaintext)]

    return ''.join(
        [encrypt_character_shift_cipher(plaintext[i], ord(key[i]) - ord('a')) for i in range(len(plaintext))])


"""
Decrypting a Vigenere cipher requires the following procedure:
1. Do a substring frequency test. 
2. Find a likely length of the substring by finding common factors of distances between substrings.
3. Generate strings generated from the plain text which has an interval of the likely length of substring.
4. Generate (likely length of key) - 1 unique strings from step 3.
5. Do a frequency analysis on the strings to find a key.
"""


def substring_frequency(plaintext):
    plaintext = treat_string(plaintext)
    n = 13
    substrings = defaultdict(list)
    for i in range(2, n):
        for j in range(len(plaintext)):
            slice_end = j + i
            # avoid slicing past text
            if slice_end > len(plaintext):
                slice_end = len(plaintext)
            if len(plaintext) - j < i:
                break

            substring = plaintext[j:slice_end]
            if substring:
                substrings[substring].append(j)

    exists = set()
    for k in reversed(sorted(substrings)):
        if tuple(substrings[k]) in exists:
            substrings[k] = []
        else:
            exists.add(tuple(substrings[k]))

    # only return substrings with more than one occurrence
    return {k: occurrences for k, occurrences in substrings.items() if len(occurrences) > 1}


def find_common_factor(substring_frequency: dict) -> defaultdict:
    factor_occurrence = defaultdict(lambda: 0)

    for occurrences in substring_frequency.values():
        # find all distances
        distances = set()
        for combination in combinations(occurrences, r=2):
            distances.add(abs(combination[1] - combination[0]))

        for distance in distances:
            for factor in factors(distance):
                if factor != 1:
                    factor_occurrence[factor] += 1

    return factor_occurrence


def decrypt_hill_ciper(plaintext: str, inverted_key: np.ndarray):
    # note input is inverted_key
    # use sympy to get inverted modulo inverse
    treat_string(plaintext)
    at_once = inverted_key.shape[0]

    def convert_to_str(a):
        s = ''
        for i in a:
            c = i[0] % 26
            s += chr(c + ord('a'))
        return s

    s = ''
    piece = []
    for i in range(len(plaintext)):
        if i % at_once == 0:
            if piece:
                s += convert_to_str(inverted_key @ np.array(piece))
            piece.clear()
        piece.append([ord(plaintext[i]) - ord('a')])
    s += convert_to_str(inverted_key @ np.array(piece))
    return s


def coincidence_rate(s: str):
    N = len(s)
    sum_ = 0

    char_frequencies = dict(frequency_analysis(s))
    for i in range(26):
        if chr(i + ord('a')) in char_frequencies:
            n_i = char_frequencies[chr(i + ord('a'))]
            sum_ += n_i * (n_i - 1)

    print('sum', sum_)
    return sum_ / (N * (N - 1))
