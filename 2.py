import string
import random

alphabet = list(string.ascii_lowercase)
num_of_letters = len(alphabet)


def letter_at(letterpos):
    return alphabet[letterpos]


for i in range(num_of_letters):
    for j in range(num_of_letters):
        for k in range(num_of_letters):
            for l in range(num_of_letters):
                for m in range(num_of_letters):
                    word = letter_at(i) + letter_at(j) + letter_at(k) + letter_at(l) + letter_at(m)
                    if word == "zzzzz":
                        print("foun")
                        exit()    