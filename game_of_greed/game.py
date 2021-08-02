from game_of_greed.game_logic import GameLogic
from game_of_greed.banker import Banker

class Game:
    def __init__(self):
        self.banker=Banker
    
    def play(self,roller=None):
   
        round_number=1
        dice_num=6
        print("Welcome to Game of Greed")
        print("(y)es to play or (n)o to decline")
        response=input("> ")
        if response=="y" or response=="yes":
            round_number+=1
            print('Starting round {round_number}')
            print("Rolling {dice_num} dice...") 
            start=GameLogic()
            rolled=start.dice(dice_num)
            print(rolled)
            user=input("Enter dice to keep, or (q)uit:")
            response=input("> ")
            if response=='q':
                    print("Thanks for playing. You earned 0 points") 
                 
            else:
                    print("OK. Maybe another time")    
        
    def roll_dice(self,num):
        print(f"Rolling {num} dice...")
        rolls=self._roller(num)
        print("*** "+" ".join([str(i)for i in rolls])+" ***")
        return rolls
            
                  
            
       

Game()
# x=Game()
# x.play()