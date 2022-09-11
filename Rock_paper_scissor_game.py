import random


print("Winning Rules of the Rock paper scissor game as follows: \n"
								+"Rock vs paper->paper wins \n"
								+ "Rock vs scissor->Rock wins \n"
								+"paper vs scissor->scissor wins \n")

while True:
	print("Enter choice \n 1 for Rock, \n 2 for paper, and \n 3 for scissor \n")
	
	
	choice = int(input("User turn: "))

	
	
	while choice > 3 or choice < 1:
		choice = int(input("enter valid input: "))
		

	
	if choice == 1:
		choice_name = 'Rock'
	elif choice == 2:
		choice_name = 'paper'
	else:
		choice_name = 'scissor'
		
	
	print("user choice is: " + choice_name)
	print("\nNow its computer turn.......")

	
	computer_choice = random.randint(1, 3)
	
	
	while computer_choice == choice:
		computer_choice = random.randint(1, 3)

	
	if computer_choice == 1:
		computer_choice_name = 'Rock'
	elif computer_choice == 2:
		computer_choice_name = 'paper'
	else:
		computer_choice_name = 'scissor'
		
	print("Computer choice is: " + computer_choice_name)

	print(choice_name + " V/s " + computer_choice_name)
	
	if choice == computer_choice:
		print("Draw=> ", end = "")
		result = "Draw"
	
	
		if((choice == 1 and computer_choice == 2) or
		(choice == 2 and computer_choice ==1 )):
			print("paper wins => ", end = "")
			result = "paper"

		elif((choice == 1 and computer_choice == 3) or
			(choice == 3 and computer_choice == 1)):
			print("Rock wins =>", end = "")
			result = "Rock"
		else:
			print("scissor wins =>", end = "")
			result = "scissor"

	
	if result == "Draw":
		print("Its a tie")
	if result == choice_name:
		print("User wins")
	else:
		print("Computer wins")
		
	print("Do you want to play again? (Yes/No)")
	ans = input().lower


	
	if ans == 'no':
		break
	

print("\nThanks for playing")
