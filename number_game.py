#Number Guessing game
hidden_number = 9
guess_count = 0

while guess_count < 3:
  guess = int(input("Guess the number: "))
  guess_count += 1
  
  if guess != hidden_number and guess_count < 3:
    print("Try again!")
    
  elif guess == hidden_number:
    print("You got it!")
    break
    
  else:
    guess_count == 3
    print("You ran out of guesses!")
    print("Game Over!")
