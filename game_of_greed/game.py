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

    def start_game(self ,round_number=1):
        self.round_number=round_number
        self.dice_num=6
        
        while self.round_number <= 6:
            print(f'Starting round {self.round_number}')
            print(f"Rolling {self.dice_num} dice...") 
            rolled=self.roller(self.dice_num)
            print("*** "+" ".join([str(i)for i in rolled])+" ***")
            print("Enter dice to keep, or (q)uit:")
            response=input("> ")
            self.round(response)
 
    def bankscore(self, round_number):
        bank_score = self.banker.bank() 
        print(f"You banked {bank_score} points in round {round_number}")           
        print(f"Total score is {self.banker.balance} points")

    def quit(self):
        print(f"Thanks for playing. You earned {self.banker.balance} points")
        sys.exit()
        
    
    def re_roll(self):
        print(f"Rolling {self.dice_num} dice...")
        rolled=self.roller(self.dice_num)
        print("*** "+" ".join([str(i)for i in rolled])+" ***")
        print("Enter dice to keep, or (q)uit:")
        response=input("> ")
        self.round(response)


    def round(self,response):
        if response=='q':
                self.quit()
        else:
            response = [int(i) for i in response]
            response_tuple=tuple(response)
            self.dice_num=self.dice_num-len(response_tuple)
            score=GameLogic.calculate_score(response_tuple)
            self.banker.shelf(score)
            print(f'You have {self.banker.shelved} unbanked points and {self.dice_num} dice remaining')
            print("(r)oll again, (b)ank your points or (q)uit:")
            response=input("> ")
            if response=='q':
                self.quit()
            else: 
                if response == 'b':
                    self.bankscore(self.round_number)
                    self.dice_num=6
                    self.round_number=self.round_number+1
                elif response == "r":
                    self.re_roll()
                elif response == 'q':
                    self.quit()
     
        
if __name__ == "__main__":
    x=Game().play()
