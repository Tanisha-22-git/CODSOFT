import random
print("Welcome to rock paper scissor game")
print()
user_score=0
computer_score=0
ties=0
name=str(input("Enter your player name  : "))
print("""
      Winning rules :
      Rock VS Scissor = Rock Wins
      Paper VS Rock = Paper Wins
      Scissor VS paper = Scissor Wins
      """)
while True:
    print(""" Choices are :
          1)Rock
          2)Paper
          3)Scissor 
""")
    choice =int(input("Enter your choice between number range from 1 to 3"))
    print()
    if choice == 1:
        user_choice = "Rock"
    elif choice == 2:
        user_choice = "Paper"
    elif choice == 3:
        user_choice = "Scissor"
    else:
        print("Invalid Choice   Please Try Again")
        continue
    computer = random.randint(1,3)
    if computer == 1:
        computer_choice = "Rock"
    elif computer == 2:
        computer_choice = "Paper"
    else:
        comp_choice = "Scissor"
    print(name,"Choice :",user_choice,"|","Computer Choice :",computer_choice)
    if(user_choice == "Rock" and computer_choice == "Scissors") or (user_choice == "Scissors" and computer_choice == "Rock"):
        result = "Rock"
    elif(user_choice == "Paper" and computer_choice == "Rock") or (user_choice == "Rock" and computer_choice == "Paper"):
        result = "Paper"
    elif(user_choice == computer_choice):
        result = "Tie"
    else:
        result = "Scissor"
    if result == "Tie":
        print()
        print("It's a Tie Round")
        ties += 1
    elif result == user_choice:
        print()
        print("You win the round")
        user_score += 1
    else:
        print()
        print("Computer win the round")
        computer_score += 1
    print()
    print("Scores Are : ")
    print("                                         ")
    print(" "*4 + name,":",user_score,"|","Computer :",computer_score,"|","Ties Are :",ties)
    print("                                          ")
    print()
    repeat = str(input("do you want to play again Yes/No :"))
    if repeat == "No" or repeat == "no":
        break
print()
if user_score > computer_score:
    print(name,"Win With",user_score,"Points!")
elif user_score < computer_score:
    print("Computer Win With",computer_score,"Points!")
else:
    print("It's a Tie! You Both Win With",ties,"Points")
print()


        

