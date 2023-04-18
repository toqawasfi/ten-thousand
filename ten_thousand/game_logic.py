import random
from collections import Counter
class GameLogic ():
 
  '''
   This class is made to contain all game methods 
   currently it contains calculate score which receives one  int parameter and roll_dice which recives tuple of number of dices to roll.
  '''     
  @staticmethod
  def calculate_score(t):
   '''
   calculate_score is a method inside of GameLogic class which is resposnible for calculting accumlative score after each roll
   this method recives one int par
   this method returns int num represents the total score.
   '''
   result = 0
   d_counter = Counter(t)

   if(d_counter[5]==1):
     result +=  50

   if (d_counter[1]==1):
     result += 100

   if(d_counter[5]==2):
      result +=  100

   if(d_counter[1]==2):
      result +=  200

   if(d_counter[2]==1 or d_counter[2]==2 ):
      result +=  0

   if(d_counter[5]==3):
      result +=  500

   if(d_counter[1]==3):
      result +=  1000

   if( d_counter[1]==1 and d_counter[2]==1 and d_counter[3]==1 and d_counter[4]==1 and d_counter[5]==1 and d_counter[6]==1):
     result =  1500

   if(d_counter[2]==3):
     result += 200

   if(d_counter[2]==4):
     result += 400

   if(d_counter[2]==5):
     result += 800

   if(d_counter[2]==6):
     result = 1600

   if(d_counter[1]==6):
     result = 8000

   if(d_counter[1]==4):
     result = 2000

   if(d_counter[1]==5):
     result += 4000

   if(d_counter[3]==1 or d_counter[3]==2):
     result += 0 

   if(d_counter[3]==3):
     result += 300

   if(d_counter[3]==4):
     result += 600

   if(d_counter[3]==5):
     result += 1200

   if(d_counter[3]==6):
     result = 2400

   if(d_counter[4]==1 or d_counter[4]==2):
     result += 0 

   if(d_counter[4]==3):
     result += 400 

   if(d_counter[4]==4):
     result += 800 

   if(d_counter[4]==5):
     result += 1600 

   if(d_counter[4]==6):
     result += 3200 

   if(d_counter[5]==4):
     result += 1000 

   if(d_counter[5]==5):
     result += 2000 

   if(d_counter[5]==6):
     result += 4000 

   if(d_counter[6]==1 or d_counter[6]==2):
     result += 0 

   if(d_counter[6]==3):
     result += 600 

   if(d_counter[6]==4):
     result += 1200 

   if(d_counter[6]==5):
     result += 2400 

   if(d_counter[6]==6):
     result += 4800 

   if(d_counter[2]==2 and d_counter[3]==2 and d_counter[6]==2 ):
     result =1500

   return result
  @staticmethod
  def roll_dice(dice_num=6):
       '''
        roll_dice is a method inside of GameLogic class which is resposnible for rolling dices basedon what the user keep .
       this method recives one int par represents number of dices to roll
       this method returns tuple represents the new number of dices.
      '''
       random_numbers = []
       
       for i in range(dice_num):
         num = random.randint(1, 6)
         random_numbers.append(num)
       tuple1=tuple(random_numbers)
       return tuple1
       
    #    while True:
    #     num_str = input("Enter a number (or 'done' to finish): ")
    #     if num_str== 'done':
    #       break
    #     nums = map(int, num_str.split())
    #     numbers = tuple(list(numbers) + list(nums))
    #     return numbers
       


    # roll_dice()  

if __name__ == "__main__":
  example1=GameLogic()
 

#   print(example1.calculate_score())
  
   
   
    
        