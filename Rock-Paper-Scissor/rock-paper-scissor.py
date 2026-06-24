import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

print("Welcome to the rock, paper and scissor gam. Thi game i based on player vs computer ")
player_choice= input("Type R for rock, P for paper and S for scissor: ").upper()

computer_choice = random.randint(1,3)

if player_choice == "R" :
    print("You choose: ")
    print(rock)
    if computer_choice == 2 :
        print("Computer choose: ")
        print(paper)
        print("Computer won. You lost.")
    elif computer_choice == 1 :
        print("Computer choose: ")
        print(rock)
        print("Game draw")
    else :
        print("Computer choose: ")
        print(scissors)
        print("You won congratulation.")

elif player_choice == "P" :
    print("You choose:")
    print(paper)
    if computer_choice == 2 :
        print("Computer choose: ")
        print(paper)
        print("Game draw")
    elif computer_choice == 1 :
        print("Computer choose: ")
        print(rock)
        print("You won congratulation.")
    else :
        print("Computer choose: ")
        print(scissors)
        print("Computer win. You lost")
else :
    print("You choose:")
    print(scissors)
    if computer_choice == 1 :
        print("Computer choose:")
        print(rock)
        print("Computer won. You lost.")
    elif computer_choice == 2 :
        print("Computer Choose:")
        print(paper)
        print("You won Congratulation")
    else :
        print("Computer choose:")
        print(scissors)
        print("Game draw")