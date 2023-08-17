class Die:
    '''A die has N sides, or “faces”, and W weights, and can be rolled to select a face.'''
    
    def __init__(self, array_of_faces, weight):

        self.array_of_faces = [*range(1, array_of_faces, 1)]
        self.weight = 1
        self.face_and_weights = pd.DataFrame({'face': self.array_of_faces, 'weight': self.weight}) 
        _final_df=pd.DataFrame(self.face_and_weights) 
              

    def change_weight(self, face, new_weight):
        "Changes weight of die face"
        self.face = face
        self.new_weight = new_weight
        #Face value check
        if face not in self.face_and_weights.face.values:
            raise ValueError(f"Face '{face}' not defined for this die.")
        
        try: #Weight is float
            new_weight=float(new_weight)
        except ValueError:
            raise ValueError(f"Weight '{new_weight}' not float/cannot be converted.")
            
        #Update
        self.face_and_weights.loc[self.face_and_weights.face == face, 'weight'] = new_weight
    
    def roll(self, n_rolls=1):
        "Rolls the the dies n number of times and returns a list of results."
        #this_weight=self.face_and_weights.weight
        return self.face_and_weights.face.sample().to_list
        
    def show(self):
        "Shows the dataframe created with current faces and weights in intializer."
        return self._final_df






    
    
import pandas as pd
from random import randint

class Game:
    '''A game consists of rolling of one or more dice of the same kind one or more times.'''

    def __init__(self, weight, num_of_die, num_of_faces):
        self.dice = [num_of_faces for _ in range(num_of_die)]
        self.num_of_faces = num_of_faces
        self.weight = weight
        num_of_die = num_of_die
        die_objects_df = pd.DataFrame()

    def roll_die(self):
        return randint(1, self.num_of_faces) #face rolled (die result of roll)
        #self.face_counter = pd.DataFrame({'face':[], 'face_count':[]})       
        
    def roll_dice(self,n): 
        total_rolls = 0
        for i in range(n):
            total_rolls += self.roll_die()
        return total_rolls
        self.total_rolls=total_rolls
        
        num_of_die = self.dice
        num_of_dice = len(num_of_die)
        _die_objects_df = pd.DataFrame(index=range(num_of_dice),columns=range(total_rolls))
        


        
        
    
    
    
    
from collections import Counter
import pandas as pd
import numpy as np

class Analyzer:
    '''An analyzer takes the results of a single game and computes various descriptive statistical properties 
    about it. These properties results are available as attributes of an Analyzer object.'''
    
    def __init__(self, num_of_sides):
        self.num_of_sides = num_of_sides
        self.face_counter = pd.DataFrame({'face':[], 'face_count':[]}) 
        self.jackpot_list = pd.DataFrame({
            'face':[], 
            'Jackpot_Count':[]})
        self.combination = pd.DataFrame({
            'face':[], 
            'Face_Count':[]})
        
    def roll(self):
        #self.rolled = randint(1, self.sides)
        face = randint(1, self.num_of_sides) #face rolled (die result of roll)
        #self.face_counter = pd.DataFrame({'face':[], 'face_count':[]}) 

    def roll_face_count(self, face, face_count):
        "Checks number of time a given face appears when rolled."
        self.face = face
        self.face_count = face_count
        new_face_counter = self.combination 
        
        #Check face and add 1 to count per roll
        if self.has_counted(face, face_count):
            self.face_counter = pd.replace({'face_count': [row_number]}, [new_face_count])
        else:
            self.face_counter = pd.concat([self.face_counter, new_face_counter], ignore_index=True)            
            
        
        # Get the number of faces, and number to roll.
    def get_init(self, num_of_sides, num_of_rolls):
        self.num_of_sides = num_of_sides
        self.num_of_rolls = num_of_rolls
        THE_Counter = pd.DataFrame({'num_of_sides':[], 'num_of_rolls':[]}) 
            
    def has_counted(self, face, face_count):
        row_number = self.face_counter.loc[self.face_counter['face'] == face]
        new_face_count = face_count + 1
        #return (self.face_counter = pd.replace({'face_count': [row_number]}, [new_face_count])
        



        
        
    def jackpot(self, face1, face2, face_count=1):
        "how many times a roll resulted in all faces being the same, e.g. all one for a six-sided die"
        #current roll
        global current_roll
        current_roll = pd.DataFrame({
            'face1': [face1], 
            'face2': [face2], 
            'face_count': [face_count]
        })
        append_ready = current_roll[[face1], [face_count]].copy()
        #record only when all faces are the same for a dice roll
        for index, rows in current_roll.iterrows():
            if (rows.face1 == rows.face2):
                #append_ready = cur_roll[[rows.face1, rows.face_count]]
                #print(append_ready)
                self.jackpot_list.append(append_ready, ignore_index = True)
            else:
                pass
     

 
    
            
    def combination(self):
        '''how many combination types of faces were rolled and their count'''
        #create dataframes for types of faces were rolled and their count
        df = pd.DataFrame({"face_combination":[], "combination_count":[]})
        df2 = df.set_index(['Face 1','Face 2', 'Face 3','Face 4', 'Face 5','Face 6','Face 7'])
        current_faces = current_roll['face']
        if df2 == current_faces:
            return False
        else:
            return df.append(current_faces)
              

        
    
    def all_face_counts(self):
        all_face_counter = pd.concat(self.combination, current_roll)
        