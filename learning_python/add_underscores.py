def add_underscores(word):
    new_word = "_"
    for letter in word:
        new_word = new_word + letter + "_"
        print(f"letter = {letter}; new_word = {new_word}")
    return new_word

phrase = "hello"
print(add_underscores(phrase))
