import random 
total_guesses = 0


random_num = random.randint(0, 100)



while True:
    guess = int(input("guess a number /n "))
    if guess < random_num:
        print("the number you want is higher")
        total_guesses += 1
    elif guess > random_num:
        print("the number you want is lower")
        total_guesses += 1
    else:
        total_guesses += 1
        print(" congrats! you guessed it")
        print("You guessed ")
        print(total_guesses)
        print(" times.")
        break
