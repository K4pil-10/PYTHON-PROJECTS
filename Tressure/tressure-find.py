print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

print ("Welcome to the Tressure Island")
print("You are at a cross the road. Where do you want to go?")
choose_1 = input("Type 'left' or 'right':  ").lower()

if choose_1 == "left" :
    print("You've come to a lake. There is an island in the middle of the lake.")
    choose_2 = input("Type 'wait' to wait for a boat. Type 'swim' to swim across. :  ").lower()
    if choose_2 == "wait" :
        print("You arrive at the island unharmed. There is a house with 3 doors.")
        choose_3 = input("One red, one yellow and one blue. Which colour do you choose? : ").lower()
        if choose_3 == "yellow" :
            print("You won.")
        elif choose_3 == "red" :
            print("Yor are burned by the fire. Game Over!")
        elif choose_3 =="blue" :
            print("Yor are eaten by beasts. Game over")
        else:
            print("You have choose a door that don't exist. Game over !")
    else :
        print("Yor are died due to attack by the Trout. Game over ! ")
else :
    print("You fell into a hole. Game Over.")
