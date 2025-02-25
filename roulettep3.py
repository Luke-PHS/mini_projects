import random
import time

def generate_wheel(): 
    spaces = []
    for i in range(18):
        spaces.append("red")
        spaces.append("black")
    for i in range(2):
        spaces.append("green")
    return spaces

def spin_wheel(spaces):
    return random.choice(spaces)

def play_game():
    money = 1000
    spaces = generate_wheel()
    
    while True:
        print("you have " + str(money) + ".")
        bet = input("HOW MUCH MONEY YOU GAMBLE ")
        bet = int(bet)
        color = input("WHAT COLOR YOU BET ON ")
        
        
        print("The wheel is SPINNING HOLD ON")
        time.sleep(2)
        landed = spin_wheel(spaces)
        print("It landed on " + landed + ".")


        if landed == color:
            money = money + bet
            print("YOU WON NOW GAMBLE AGAIN WITH YOUR MONEY OF " + str(money))
        else:
            money = money - bet
            print("HAHAHAH YOU LOST NOW YOU HAVE " + str(money))
        

        play_again = input("DO YOU WANT TO GAMBLE MORE ")
        if play_again == "no":
            break
play_game()