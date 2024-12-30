from random import randint

#Generate a random number between 1 and 100
rng = randint(1,100)
count = 0

while count < 5:
    #Ask the user to guess the number
    guess = input("Guess the number bettwenn 1 to 100: ")
    if not int(guess):
        print("Invalid input")
        continue
    guess = int(guess)
    if rng == guess:
        print("Correct!")
        break
    elif rng > guess:
        print("Too low!")
        count += 1
    else:
        print("Too high!")
        count += 1

if count >= 5:
    print("You lose! The number was: ", rng)
else:
    print(f"You win! with {count+1} attempts")

