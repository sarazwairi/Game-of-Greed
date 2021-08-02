import random
from collections import Counter

class GameLogic:
    @staticmethod
    def calculate_score(numbers):
        score=0
        dice_counter = Counter(numbers)
        commnest=dice_counter.most_common()

        for item in commnest:
        
                if len(dice_counter) == 6:
                    score+=1500
                    return score
                elif len(dice_counter)==3 and commnest[0][1]==2:
                    score+=1500
                    return score
                elif item[1] == 5:
                    if item[0] == 1:
                        score += 3000
                    else:
                        score += item[0] * 300
                elif item[1] == 4:
                    if item[0] == 1:
                        score += 2000
                    else:
                        score += item[0] * 200
                elif item[1] == 3:
                    if item[0] == 1:
                        score += 1000
                    else:
                        score += item[0] * 100
                elif item[1] == 2:
                    if item[0] == 1:
                        score += 200
                    elif item[0] == 5:
                        score += 100
                elif item[1] == 1:
                    if item[0] == 1:
                        score += 100
                    elif item[0] == 5:
                        score += 50
                elif len(dice_counter) == 1 and commnest[0][1] == 6 :
                    if commnest[0][0]==1:
                        score+=4000
                    else:
                        score += commnest[0][0]*400


        return score

    





    @staticmethod
    def roll_dice(value):
        nums_list=[]
        for i in range(value):
            nums_list.append(random.randint(1,6))

        return tuple(nums_list)
    
    
    # lst=(1,2,3,4,5,6)
    # print(Counter(lst))