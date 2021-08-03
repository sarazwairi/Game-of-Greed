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
    def get_scorers(input):
        ## tuple--->tuple
        calculate=Counter(input)
        if len(calculate)==6:#straight
            return input
        if len(calculate)==3:#pairs
            if all(value ==2 for value in calculate.values()):
                return input
        result=[]

        for number,count in calculate.items():
            if count>=3:
                result+=[number]*count
            elif number==1 or number==5:
                result+=[number]*count
        return result

    @staticmethod
    def validate_keepers(dice_list, dice_input):
        output_one = Counter(dice_input).most_common()
        output_two = Counter(dice_list).most_common()
        if len(output_one) > len(output_two):
          return True
        result=[]
        valid_game = False
        for i in output_one:
             for j in output_two:
                 if i[0] == j[0]:
                     if i[1] <= j[1]:
                          result.append(1)
        if len(output_one) == len(result):
            valid_game = True
        return valid_game




    @staticmethod
    def roll_dice(value):
        nums_list=[]
        for i in range(value):
            nums_list.append(random.randint(1,6))

        return tuple(nums_list)
    
    
