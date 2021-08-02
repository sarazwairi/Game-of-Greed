from game_of_greed.game_logic import GameLogic
from game_of_greed.banker import Banker

class Game:
    def __init__(self,rounds=6):
        self.banker=Banker
        self.rounds=rounds    
    
    def play(self,roller=None):

        self.round_number=0
        self._roller=roller or GameLogic.roll_dice

        print("Welcome to Game of Greed")
        print("(y)es to play or (n)o to decline")
        response=input("> ")
        if response=="y" or response=="yes":
            print("ok")
        else:
            print("OK. Maybe another time")

Game()