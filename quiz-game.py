# Let's make quiz game :)

print("Welcome to my computer quiz!")

playing = input("Do you want to play? ").lower()

# if the condition is True  it will move on to the game
if playing != "yes":
    quit()

print("Okay! Let's play :) ")

score = 0

# qns - 1
answer = input("What does CPU stands for? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1  # incrementation of score
else:
    print("Incorrect!")

# qns - 2    
answer = input("What does GPU stands for? ")
if answer.lower() == "graphics processing unit":
    print("Correct!")
    score += 1    # incrementation of score
else:
    print("Incorrect!")

# qns - 3
answer = input("Python is a ? ")
if answer.lower() == "high level programming language":
    print("Correct!")
    score += 1   # incrementation of score
else:
    print("Incorrect!")

# qns - 4
answer = input("What does PSU stans for? ")
if answer.lower() == "power supply unit":
    print("Correct!")
    score += 1   # incrementation of score
else:
    print("Incorrect!")

# qns - 5
answer = input("What is the keyboard shortcut of Save? ")
if answer.lower() == "ctrl+s":
    print("Correct!")
    score += 1    # incrementation of score
else:
    print("Incorrect!")

# Total score
print("You got " + str(score) + " questions correct!!")
# Percentage of the score
print("You got " + str(score/5 * 100) + "%." )