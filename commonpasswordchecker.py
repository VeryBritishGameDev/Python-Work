guess_word = "uscwap"

f = open("10millioncodes.txt")


lines = f.readlines()
words = [word.strip() for word in lines]

if guess_word in words:
    print(f"found word {guess_word}")
    print(words.index(guess_word))