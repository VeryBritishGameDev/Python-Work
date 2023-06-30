import string
alphabet = list(string.ascii_letters)

word_to_guess = "bobth"

## cycle through each letter
## _ _ _ _ _ 

num_of_letters = len(alphabet)


def letter_at(letterpos):
    return alphabet[letterpos]     

def guess_password():


    # YOUR CODE HERE

    for i in range(num_of_letters):
        for j in range(num_of_letters):
            for k in range(num_of_letters):
                for l in range(num_of_letters):
                    for m in range(num_of_letters):
                        word = letter_at(i) + letter_at(j) + letter_at(k) + letter_at(l) + letter_at(m)
                        if word == word_to_guess:
                             return f"your word is {word}"


    return "cant find"

print(guess_password())