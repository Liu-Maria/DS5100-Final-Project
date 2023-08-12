class Die:
    
    def faces(self, face):
        self.face_df=[self.face]
        _final_df=pd.DataFrame(self.face_df)

    def change_weight(self, face, new_weight):
        "Changes weight of die face"

        #Face value check
        if side_face not in self.die.face.values:
            raise ValueError(f"Face '{side_face}' not defined for this die.")
        
        try: #Weight is float
            side_weight=float(side_weight)
        except ValueError:
            raise ValueError(f"Weight '{side_weight}' not float/cannot be converted.")
            
        #Update
        self.die.loc[self.die.face == side_face, 'weight'] = side_weight
    
    def roll(self, n_rolls=1):
        "Rolls the the dies n number of times and returns a list of results."
        return self.die.face.sample(n_rolls, weights=self.die.weight, replace=True).to_list
        
    def show(self):
        "Shows the dataframe created with current faces and weights in intializer."
        return self._final_df





    
    
class Game:
    '''A game consists of rolling of one or more dice of the same kind one or more times.'''
    def dice(self, die_objects):
        self.die_objects_df = pd.DataFrame(self.die_objects)
        die_sides=self.die.face
        if die_sides is not self.game.die_objects.values:
            raise ValueError(f"Sides '{die_sides}' not equal.")
        #only the most recent roll
        return self.die_objects_df
    
    
    
    
from collections import Counter
import pandas as pd

class Analyzer:
    '''An analyzer takes the results of a single game and computes various descriptive statistical properties 
    about it. These properties results are available as attributes of an Analyzer object.'''

    def roll_face_count(self, face, face_count):
        "Checks number of time a given face appears when rolled."
        self.face = face_count + 1
        new_face_count = self.face_count
        new_face_count = new_face_count + 1
        #Check face and add 1 to count per roll
        
        # Get the number of faces, and number to roll.
        dice_face = get_int("Select the number of faces you want your dice to have: ")
        dice_amount = get_int("Select how many dices of the given faces you want to roll: ")
        face_count = Counter()
        for i in range(dice_amount):
            roll = random.randint(1, dice_face)
            print(f"Die {i}: {roll}")  # N.B. May want to add capability to disable this for large numbers of rolls (e.g > 10)
            num[roll] += 1

        
    def jackpot(self):
        "how many times a roll resulted in all faces being the same, e.g. all one for a six-sided die"
        #create dataframe
        jackpotdf = pd.DataFrame()
        #record only when all faces are the same for a dice roll
        faces_list = self #make all faces on a roll into a list
        faces_set = set(faces_list) #make list of faces into a set
        if set(faces_list) == 1:
            jackpotdf.append(1)
        elif set(faces_list) != 1:
                jackpotdf.append(0)
        
            
    def combination(self):
        '''how many combination types of faces were rolled and their count'''
        #create dataframes for types of faces were rolled and their count
        df = pd.DataFrame("face_combination", "combination_count")
        face_combo = self.faces 
        a = df['face_combination']
        row_num = df[df['face_combination'] == 'face_combo'].index 
        #in case of new face commbination
        new_count = df[df['combination_count']+1]
        df.loc[df['face_combination'] == face_combo] = df.replace(df['face_combination'][row_num],new_count)   
        #add one to old count of this face combo
        df.loc[df['face_combination'] != face_combo] = df.append({face_combo, 1})