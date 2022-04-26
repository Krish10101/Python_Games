import random

top_of_range = input("Type a number: ")

if top_of_range.isdigit():
  top_of_range = int(top_of_range)

  if top_of_range <= 0:
    print("Please type a number greater than 0 next time.")
    quit()

else:
  print("Please type a number next time.")
  quit()

## random.randrange(-6, 11)   -Range does not include the last number

random_number = random.randint(0, top_of_range)  ## this would include the last number which is 11 in our case

guesses = 0

while True:
    guesses += 1
    user_guess = input("Make a guess: ")

    if user_guess.isdigit():
      user_guess = int(user_guess)
    else:
      print("Please type a number next time.")
      continue

    if user_guess == random_number:
      print("You have got it right!")
      break
    elif user_guess <= random_number:
      print("You got it wrong! the number is geater")
    else:
      print("You got it wrong! the number is smaller")
    
print("You have guessed the right number in ", guesses , " attempts")

