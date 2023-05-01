from game_logic import GameLogic
# ten_thousand.
from collections import Counter

def play(roller=GameLogic.roll_dice, num_round=15):

    score = 0
    global dice_roller
    dice_roller = roller
    total =0

    def start_game(num_round):
        nonlocal score
        dec_round = 0
        nonlocal total
        def bank(num):
            nonlocal score
            if(num_round==1):
              score = num
              print("You banked " + str(num) + " points in round " + str(dec_round))
              print("Total score is " + str(score) + " points")
            else:
                nonlocal total 
                total+=score
                print("You banked " + str(num) + " points in round " + str(dec_round))
                print("Total score is " + str(total) + " points")

           

        def quit():
            nonlocal values
            print("Thanks for playing. You earned " + str(total) + " points")

        while num_round > 0:
          

            dec_round += 1
            num_dice = 6
           
            print("Starting round " + str(dec_round))
            values = dice_roller(6)
            formatted_roll = format_roller(values)
            print("Rolling 6 dice...")
            print(formatted_roll)
            print("Enter dice to keep, or (q)uit:")
            
           
            input2 = input("> ")
            rem_input2 = input2.replace("> ", "").strip()
            if rem_input2 == "q":
                quit()
                return 
            else:
                # bank_count_int=int(rem_input2)
                
                # if len(rem_input2)==1:
                    bank_count_int=int(rem_input2)
                    dices_rem = dice_roller(num_dice)
                    score = GameLogic.calculate_score((int(rem_input2),))
                    num_dice -= 1
                # if(tuple(rem_input2) not in values  ):
                #       print("Cheater!!")
                    
                # else:
                    list_num = [int(d) for d in rem_input2]
                    t= tuple(list_num)
                    score = GameLogic.calculate_score(t)
                    num_dice -= len(rem_input2)
                    dices_rem = dice_roller(num_dice)
                    
                    for roll in t:
                        if roll  not in values:
                             print("Cheater!!")
                    user_counter = Counter(t)
                    # values_counter = Counter(values)
                    rem_counter = Counter(dices_rem)
                    # if (user_counter[1]>=rem_counter[1]):
                    #      print("Cheater!!")

                    for  i in range(1,7):
                        if (user_counter[i]>rem_counter[i] and user_counter[i]!=0):
                           print("Cheater!!")



                # score = GameLogic.calculate_score(rem_input2)
                banked_count = score
                print("You have " + str(banked_count) + " unbanked points and " + str(num_dice) + " dice remaining")
                print("(r)oll again, (b)ank your points or (q)uit:")

                input3 = input("> ")
                rem_input3 = input3.replace("> ", "").strip()
                if rem_input3 == "b":
                    bank(banked_count)
                    # num_dice=
                elif rem_input3 == "q":
                    quit()
                # elif rem_input3 == "r":
                #     dices_rem = dice_roller(num_dice)
            
            num_round -= 1
            num_dice = 0
            # num_dice -= 1

           
    # def cheat():
       

    def user_input():
        print("Welcome to Ten Thousand")
        print("(y)es to play or (n)o to decline")
        input1 = input("> ")
        rem_input1 = input1.replace("> ", "").strip()
        return rem_input1

    user = user_input()
    if user == "y":
        start_game(num_round)
    else:
        print("OK. Maybe another time")
    

def format_roller(dice_roller):
    as_string = [str(value) for value in dice_roller]   
    format_roll = " ".join(as_string)
    return f"*** {format_roll} ***"
    
if __name__ == "__main__":
    play()
 