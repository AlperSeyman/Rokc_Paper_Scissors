import random


actions = ['rock','paper','scissors']
print("Actions: ",actions)

players_score = 0
computer_score = 0

total_rounds = int(input("How many rounds do you want to play? Please enter a number:"))

round_counter = 0
print("Actions: ",actions)

while True:
  round_counter +=1
  print("Round Number:",round_counter)

  
  computer_choice = random.choice(actions)

  
  player_choice = input("Please choose your action: ")

  
  print(f"Computer Choice: {computer_choice} Player Choice: {player_choice}")



  
  if computer_choice == player_choice:
    print("TIE")

  
  elif computer_choice == "paper":
    if player_choice == "rock":
      print("Winner is: Computer")
      computer_score +=1 
    else:
      print("Winner is: Player")
      players_score +=1
  elif computer_choice == "rock":
    if player_choice == "scissors":
      print("Winner is: Computer")
      computer_score +=1
    else:
      print("Winner is: Player")
      players_score +=1
  elif computer_choice == 'scissors':
    if player_choice == 'paper':
      print("Winner is: Computer")
      computer_score +=1
    else:
      print("Winner is: Player")
      players_score +=1
  
  if round_counter == total_rounds:
    break



if computer_score == players_score:
  print(f"There is no winner. Computer Score == Player Score: {computer_score}")
elif computer_score > players_score:
  print(f"Computer is a winner.  Computer Score: {computer_score} Player Score: {players_score}")
elif computer_score < players_score:
  print(f"Player is a winner.  Computer Score: {computer_score} Player Score: {players_score}")
