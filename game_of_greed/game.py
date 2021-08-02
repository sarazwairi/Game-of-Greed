from game_of_greed.game_logic import GameLogic
from game_of_greed.banker import Banker

class Game:
    def __init__(self):
        self.banker=Banker
    
    def play(self,roller=None):
        roller=roller or GameLogic.roll_dice
   
        round_number=0
        dice_num=6
        print("Welcome to Game of Greed")
        print("(y)es to play or (n)o to decline")
        response=input("> ")
        if response=="y" or response=="yes":
            round_number+=1
            print(f'Starting round {round_number}')
            print(f"Rolling {dice_num} dice...") 

            rolled=roller(dice_num)
            print("*** "+" ".join([str(i)for i in rolled])+" ***")

            print("Enter dice to keep, or (q)uit:")
            response=input("> ")
            if response=='q':
                    print("Thanks for playing. You earned 0 points") 
                 
            else:
                    print("OK. Maybe another time")    

            
                  
            
       

Game()
x=Game()
x.play()