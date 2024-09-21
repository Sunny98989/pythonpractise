import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""
scissor ="""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

possibilities = [rock, paper, scissor]
i = random.randint(0,2)
computer_choice = possibilities[i]

while True:
    player_choice = input(
                          "TYPE EXIT TO QUIT THE GAME\n"
                            "your choice: ").lower()

    if player_choice == "exit".lower():
        print("Good bye")
        break

    if player_choice == "rock" and computer_choice == rock:
        print("you choose:", rock)
        print("computer choose:",computer_choice)
        print("draw")

    if player_choice == "rock" and computer_choice == paper:
        print("you choose:", rock)
        print("computer choose:",computer_choice)
        print("you loose")

    if player_choice == "rock" and computer_choice == scissor:
        print("you choose:", rock)
        print("computer choose:",computer_choice)
        print("You win")

    if player_choice == "paper" and computer_choice == scissor:
        print("you choose:", paper)
        print("computer choose:",computer_choice)
        print('\nyou loose\n')

    if player_choice == "paper" and computer_choice == rock:
        print("you choose:", paper)
        print("computer choose:",computer_choice)
        print('\nyou win\n')

    if player_choice == "paper" and computer_choice == paper:
        print("you choose:", paper)
        print("computer choose:",computer_choice)
        print('\nyou draw\n')

    if player_choice == "scissor" and computer_choice == paper:
        print("you choose:", scissor)
        print("computer choose:",computer_choice)
        print('\nyou win\n')

    if player_choice == "scissor" and computer_choice == rock:
        print("you choose:", scissor)
        print("computer choose:",computer_choice)
        print('\nyou loose\n')

    if player_choice == "scissor" and computer_choice == scissor:
        print("you choose:", scissor)
        print("computer choose:",computer_choice)
        print('\ndraw\n')