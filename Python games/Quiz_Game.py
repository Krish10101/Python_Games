print('welcome to my Quiz Game')

playing = input('Do you want to play? ')

if playing.lower() != 'yes':
  print("See you next time :) ")
  quit()

print("Let's play")

score = 0

answer = input("What does CPU stands for? ")
if answer.lower() == "central processing unit": ## .lower will convert the user input into lower cases.
  print("Correct")
  score += 1
else:
  print("Incorrect")

answer = input("What does GPU stands for? ")
if answer.lower() == "graphics processing unit":
  print("Correct")
  score += 1
else:
  print("Incorrect")

answer = input("What does RAM stands for? ")
if answer.lower() == "random access memory":
  print("Correct")
  score += 1
else:
  print("Incorrect")

answer = input("What does PSU stands for? ")
if answer.lower() == "power supply unit":
  print("Correct")
  score += 1
else:
  print("Incorrect")

print("You got " + str(score) + " questions correct.")  ## Converting score into string so we can add it with other string.
print("You got " + str(score/4 * 100) + "%", "score")