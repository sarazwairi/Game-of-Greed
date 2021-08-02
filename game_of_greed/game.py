from game_of_greed.game_logic import GameLogic
from game_of_greed.banker import Banker

class Game(Banker):
    # def __init__(self):
    #     # self.banker=Banker
    
    def play(self,roller=None):
        self.roller=roller or GameLogic.roll_dice
   
        
        print("Welcome to Game of Greed")
        print("(y)es to play or (n)o to decline")
        response=input("> ")
        if response=="y" or response=="yes":
            self.start_game()

        else:
            self.decline_game() 
    

    def decline_game(self):
        print("OK. Maybe another time")

    def start_game(self):
        round_number=1
        dice_num=6
        while round_number <= 6:

            print(f'Starting round {round_number}')
            print(f"Rolling {dice_num} dice...") 

            rolled=self.roller(dice_num)
            print("*** "+" ".join([str(i)for i in rolled])+" ***")
            round_number=round_number+1
            print("Enter dice to keep, or (q)uit:")
            response=input("> ")
            if response=='q':
                print("Thanks for playing. You earned 0 points")
            
            else:
                
                response_tuple=tuple(response)
                dice_num=dice_num-1
                score=GameLogic.calculate_score(response_tuple)
                print(f'You have {Banker().shelved} unbanked points and {dice_num} dice remaining')
                # Banker()


        
Game()
x=Game().play()
# score=GameLogic.calculate_score([5])
# print(score)


                  
            
       
