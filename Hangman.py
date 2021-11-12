import random

dictionary = ["cat", "dog", "hungry", "guy", "donut", "picture"]

word = random.choice(dictionary)

user_word = ["_"] * len(word)

while "_" in user_word:
    print(user_word)
    char = input("Guess a letter")
    for i in range(len(word)):
        if word[i] == char:
            user_word[i] = char
