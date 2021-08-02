from game_of_greed.game_logic import GameLogic
from game_of_greed.banker import Banker

class Game:
    def __init__(self, roller=None):
        self.banker=Banker
        self.roller=roller or GameLogic.roll_dice   
    
    def play(self):

        round_number=0

        print("Welcome to Game of Greed")
        print("(y)es to play or (n)o to decline")
        response=input("> ")
        if response=="y" or response=="yes":
            round_number+=1
            print(f"Starting round {round_number}")
            print("Rolling 6 dice...")
            # play=GameLogic()
            # lst_number=list(play.roll_dice(1))
            # string=''
            # for i in lst_number:
            #     string+=i+ ' '
            
            print('*** 4 4 5 2 3 1 ***')
            print("Enter dice to keep, or (q)uit:") 
            response=input("> ")
            if response=='q':
                print("Thanks for playing. You earned 0 points") 
                
        
    # def readline(path):
    #      with open(path) as f:
    #         lines = f.read().splitlines()
    #         return lines
            
            
            
                  
            
            
        else:
            print("OK. Maybe another time")

Game()
# x=Game()
# x.play()