target = 159
print("You have three chances to guess.")
i=1
while i<=3:
    guess = int(input(f"Enter your guess {i}: "))
    if guess == target:
        print("You win!")
        break
    elif i == 3:
        print("You lose!")
    elif guess < target:
        print("Go higher")
    elif guess > target:
        print("Go lower")
    i+=1