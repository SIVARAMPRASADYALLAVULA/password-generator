import random
choices = ["rock","paper","scissors"]
user_score = 0
computer_score = 0
while True:
    user = input("\nEnter rock,paper,or scissors:").lower()
    if user not in choices:
        print("Invalid choice! Try again")
        continue
    computer=random.choice(choices)
    print("You chose:",user)
    print("computer chose:",computer)
    if user == computer:
        print("it's a tie!")
    elif(user == "rock" and computer == "scissors") or (user == "paper" and computer =="rock") or (user == "scissors" and computer == "paper"):
        print("You Win!")
        user_score += 1
    else:
        print("Computer wins!")
        computer_score += 1
    print(f"score -> You:{user_score} | Computer:{computer_score}")
    play_again = input("Play again?(yes/no):").lower()
    if play_again != "yes":
        break
print("Thanks for playing!")