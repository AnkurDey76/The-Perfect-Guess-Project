from email.mime import image


import random
randno=random.randint(1,100)
userGuess=None
Guesses=0
while(randno!=userGuess):
  userGuess=int(input("Enter your guess: "))
  Guesses+=1
  if randno==userGuess:
    print("Damn woah! you guessed it right")
  else:
       if(userGuess>randno):
           print("ohh no! you guessed it wrong...Try a Smaller Number")
       else:
           print("ohh no! you guessed it wrong...Try a Larger Number")



print(f"Congratualations! so you've guessed the correct number in {Guesses} guesses")



#--------------------------------------------------------------------------------------

with open('highscore.txt', "r") as f:
    highscore=int(f.read())

if Guesses<highscore:
    print("Congo!--You've just broken the highscore record")
    with open('highscore.txt', "w") as f:
        highscore=f.write(str(Guesses))