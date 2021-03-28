# This game asks how many apples you would like to eat.
# If you eat too many, it will say you are sick.
# If you eat the magic number (21) you win!


def the_game():

    apples_first = int(input("How many apples would you like to eat?"))
    apples_sum = apples_first

    if int(apples_first) <=0:
        print("Don't be so negative.")

    else:
        print("You've had",apples_first,"apples.")

        while apples_sum < 21 :
            more_apples = input("Would you like to eat more?")

            if more_apples == "yes" or more_apples == "Yes":
                apples_to_add = int(input("How many more?"))
                apples_sum = apples_to_add + apples_sum
                print("You now have",apples_sum,"apples. Yum!")
            else:
                print("Too bad. They're delicious.")
                replay()
            
        else:
            if apples_sum == 21:
                print("You've eaten the magic numbner of apples. Congratulations!")
                replay()

            else:
                print("You've had",apples_sum -21,"too many apples and got a stomach ache. Sorry, you lose.")
                replay()

# This section gives the player the option to play the game again.
def replay():
    replay_choice = input("Would you like to play again? Y/N:  ")
    if replay_choice == "Y" or replay_choice == "y":
        print("Good choice,",player_name,". Let's do this again!")
        the_game()
    if replay_choice == "N" or replay_choice == "n":
        print("Thanks for playing.")
    else:
        print("Invalid response, please type Y or N to play again.")
        replay()

## This is where the game is played:

player_name = input("What is your name?")

print("Welcome to the Apple Grove,",player_name,".")

the_game()