import random
 
class GameLogic:
    pass

    @staticmethod
    def roll_dice(value):
        nums_list=[]
        for i in range(value):
            nums_list.append(random.randint(1,6))

        return tuple(nums_list)