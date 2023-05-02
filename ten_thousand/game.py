from ten_thousand.game_logic import GameLogic
# ten_thousand.
score = 0
total = 0
# rounds=15



rounds=15

def play(roller=GameLogic.roll_dice):
    '''
    play method responsible for operating the game
    args:
    receives a function to roll dice and generates 6 numbers
    returns:
    The Game with different Edge cases
    '''
    global total
    total = 0
    print("Welcome to Ten Thousand")
    print("(y)es to play or (n)o to decline")
    user_input = input("> ")
    if user_input.lower() != "y":
        print("OK. Maybe another time")
        return
    
    for num_round in range(1, 4):
        print(f"Starting round {num_round}")
        num_dice = 6
        round_score = 0
        while True:
            dice = roller(num_dice)
            # print(dice)
            print("Rolling " + str(num_dice) + " dice...")
            formatted_roll = format_roller(dice)
            print(formatted_roll)
           
            if GameLogic.calculate_score(dice) == 0:
             print("****************************************")
             print("**        Zilch!!! Round over         **")
             print("****************************************")
             print(f"You banked 0 points in round {num_round}")
             print(f"Total score is {total} points")
             num_round +=1
             print(f'Starting round {num_round}')
             point = 0
             num_dice = 6
             continue
            
            input_str = input("Enter dice to keep, or (q)uit:\n> ")
            if input_str == "q":
                print(f"Thanks for playing. You earned {total} points")
                return
            kept_dice = tuple(int(d) for d in input_str.replace(" ","") if d.isdigit())
            
            val = GameLogic.validate_keepers(dice,kept_dice)
            while (val==False):
                print("Cheater!!! Or possibly made a typo...")
                print("*** ", " ".join(str(d) for d in dice), " ***")
                input_str = input("Enter dice to keep, or (q)uit:\n> ")
                if input_str == "q":
                 print(f"Thanks for playing. You earned {total} points")
                 return
                else:
                    kept_dice = tuple(int(d) for d in input_str.replace(" ","") if d.isdigit())
                    val = GameLogic.validate_keepers(dice,kept_dice)
                    hot_check = GameLogic.get_scorers(kept_dice)

                    if len(hot_check) == 6 and not val:

                     choice = hot_dice_fun(kept_dice, unbanked_score)
                
                
 
            round_score += GameLogic.calculate_score(kept_dice)
            num_dice -= len(kept_dice)
            unbanked_score = round_score + total
            print(f"You have {round_score} unbanked points and {num_dice} dice remaining")
            input_str = input("(r)oll again, (b)ank your points or (q)uit:\n> ")
            if input_str == "b":
                total += round_score
                print(f"You banked {round_score} points in round {num_round}")
                print(f"Total score is {total} points")
                break
            elif input_str == "q":
                print(f"Thanks for playing. You earned {total} points")
                return
            elif input_str == "r":
                continue
            else:
                print("Invalid input. Try again.")

            def hot_dice_fun(kept_dice, unbanked_score,num_round):
              round_score = GameLogic.calculate_score(kept_dice)
              unbanked_score += round_score
              num_dice = 6
              print(f"You have {unbanked_score} unbanked points and 6 dice remaining")

    print(f"Thanks for playing. You earned {total} points")
           
    # user = user_input()
    # if user == "y":
    #   start_game()
    # else:
    #  print("OK. Maybe another time")
   


def format_roller(dice_roller):
    '''
    format_roller a method to reformat the input shape to match the sim file
    Args:
    receives an var(tuple) holds the value of the rolling dice
    Returns:
    the new format of the input
    '''
    as_string = [str(value) for value in dice_roller]   
    format_roll = " ".join(as_string)
    return f"*** {format_roll} ***"
    
if __name__ == "__main__":
    play()
 