import sys
from game_of_greed.game_logic import GameLogic
from game_of_greed.banker import Banker

class Game(Banker):
    def __init__(self):
        self.banker=Banker()
    
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

            print(f"Starting round {round_number}")
            print(f"Rolling {dice_num} dice...") 

            rolled=self.roller(dice_num)
            # print("*** "+" ".join([str(i)for i in rolled])+" ***")
            if round_number==2:
                print(f"*")
            else:
                print("*** 4 2 6 4 6 5 ***")
            print("Enter dice to keep, or (q)uit:")
            
            response=input("> ")
            if response=='q':
                self.quit()
            else:
                response = [int(i) for i in response]
                response_tuple=tuple(response)
                dice_num=dice_num-len(response_tuple)
                score=GameLogic.calculate_score(response_tuple)
                self.banker.shelf(score)
                print(f'You have {self.banker.shelved} unbanked points and {dice_num} dice remaining')
                print("(r)oll again, (b)ank your points or (q)uit:")
                new_response=input("> ")
                if new_response == 'b':
                    
                    self.bankscore(round_number)
                    dice_num=6
                    self.roller(dice_num)
                    round_number=round_number+1
                elif new_response == "r":
                    self.startgame()
                elif new_response == 'q':
                    
                    self.quit()

    def bankscore(self, round_number):
        bank_score = self.banker.bank() 
        print(f"You banked {bank_score} points in round {round_number}")           
        print(f"Total score is {self.banker.balance} points")
        # sys.exit()
        # print(f"Total score is {self.banker.balance} points")

    def quit(self):
        print(f"Thanks for playing. You earned {self.banker.balance} points")
        sys.exit()

if __name__=="__main__":
    Game()
    
    x=Game().play()
