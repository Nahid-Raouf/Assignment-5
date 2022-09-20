import random
print("\nWelcome to Rock Paper Scissors game")
coun=0
person1=0
person2=0

while True:
    select=int(input("\n\nDo you want to play 1)singles or 2)doubles? \n3)exit \n... "))

    if select==1:
        selectend_I=int(input("\nhow many laps? \n1_win or 3_win or 5_win \n... "))
        
        while True:
            #1)Rock 2)Paper 3)scisso)
            Computer=random.randint(1,3)
            print('-'*20)            
            print("1)Rock 2)Paper 3)scissor")
            person=int(input("Rock or Paper or scissor:"))

            if (person==1) or (person==2) or (person==3):
                if Computer==person:
                    print("\nOh, you had an equal chance, please try again ")
                elif (Computer==1 and person==3) or  (Computer==2 and person==1) or (Computer==3 and person==2):
                    print("\n sorry, the computer won ")    
                else:
                    print("\nYou win my friend :) ")
                    coun +=1
            else:
                print("The entered number is not correct, please be more careful!")
                continue

            if selectend_I==coun:
                print("Congratulations, my friend, you won the game ")
                break
            else:
                continue

    elif select==2:
        selectend_II=int(input("\nhow many laps? \n1_win or 3_win or 5_win \n... "))

        while True:
            print('-'*20)            
            print("\n1)Rock 2)Paper 3)scissor ")
            
            I=int(input("\nChoose the first player \nRock or Paper or scissor:"))
            II=int(input("\nChoose the second player \nRock or Paper or scissor:"))

            if ((I==1) or (I==2) or (I==3))and((II==1) or (II==2) or (II==3)):
                if I==II:
                    print("\nOh, you had an equal chance, please try again ")
                    continue
                elif (I==1 and II==3) or  (I==2 and II==1) or (I==3 and II==2):
                    print("\nYou are the first player to win :) ")
                    person1+=1
                else:
                    print("\nYou are the second player to win :)")
                    person2+=1
            else:
                print("The dear player entered number is not correct, try again")
            
            if selectend_II==person1:
                print(" the first player won the game")
                break
            elif selectend_II==person2:
                print("the second player won the game")
                break
            else:
                continue

    elif select==3:
        print("\ngoodbye")
        break

    else:
        print("The entered number is not correct, please be more careful!")
        continue

