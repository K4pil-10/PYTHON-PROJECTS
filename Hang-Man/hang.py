import random
from sys import displayhook
from word_list import words
from lives_visual import hang_man_art
from lives_visual import logo


lives= 6

print(logo)
chosen_word = random.choice(words)

placeholder= ""
word_length = len(chosen_word)
for word in range(word_length):
    placeholder += "_"
print(placeholder)


correct_letter= []
game_over= False
while not game_over:
    print(f"****************************{lives}/6 LIVES LEFT****************************")
    guess= input("Guess a letter: ").lower()

    if guess in correct_letter:
        print(f"You have already guessed! {guess}")
    display = ""
    for letter in chosen_word:
        if letter == guess:
            display += guess
            correct_letter.append(guess)
        elif letter in correct_letter:
            display += letter
        else:
            display += "_"
    print(display)

    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in word. You lose your life")
        if lives ==0:
            game_over= True
            print(f"***********************YOU LOSE. The word was {chosen_word}**********************")



    if "_" not in display:
        game_over= True
        print("****************************YOU WIN****************************")

    print(hang_man_art[lives])