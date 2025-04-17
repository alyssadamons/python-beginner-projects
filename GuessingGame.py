import random

word_pool = ["Elephant", "Giraffe", "Lion", "Rhino", "Zebra"]

word = random.choice(word_pool).lower()

guessedWord = ['_'] * len(word)

attempts = 10

print("Welcome to the ✨Guessing Game!✨  \nYou will be guessing the letters of a name of a wild animal.\nYou have 10 attempts. \nGood luck!")
while attempts > 0:
    print("\nCurrent Word: " + " ".join(guessedWord))

    guess = input("Guess a letter: ")

    if guess in word:
        for i in range (len(word)):
            if word[i] == guess:
                guessedWord[i] = guess
        print("Good guess!")
    else:
        attempts -=1
        print("Incorrect guess! Attempts left: " +str(attempts))

    if "_" not in guessedWord:
        print("Congratulations, you've guessed correctly. The word is: " + word)
        break
    elif attempts == 0:
        print("Sorry, you've run out of attempts. The word is " + word)






