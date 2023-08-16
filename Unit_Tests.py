#Test Die

import unittest

class DieTestSuite(unittest.TestCase):

    def test_1_get_array(self):
        die = Die(6, 1)
        test_face = 3
        test_weight = 2
        die.change_weight(test_face, test_weight)
        self.assertFalse(die.change_weight(test_face, test_weight))

    def test_2_roll(self):
        die = Die(6, 1)
        self.assertTrue(die.roll())

if __name__ == "__main__":
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
    
    

    
    
#Test Game

import unittest

class GameTestSuite(unittest.TestCase):

    def test_1_roll_dice(self):
        game = Game(1, 2, 6)
        test_number_of_rolls = 5
        game.roll_dice(test_number_of_rolls)
        self.assertTrue(game.roll_dice(test_number_of_rolls))

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
    
    
    
    
    
#Test Analyzer

import unittest

class AnalyzerTestSuite(unittest.TestCase):

    def test_1_get_face(self):
        analyzer = Analyzer(6)
        test_face = 5
        analyzer.roll_face_count(analyzer, test_face)
        self.assertFalse(analyzer.roll_face_count(analyzer, test_face))

    def test_2_jackpot(self):
        analyzer = Analyzer(6)
        test_faces_up = [
            (1),
            (5),
            (3),
            (2),
            (5),
            (7)
        ]
        for faces in test_faces_up:
            analyzer.jackpot(faces)
            
        self.assertTrue(test_faces_up, analyzer.jackpot(test_faces_up))

    def test_3_combination(self):
        analyzer = Analyzer(6)
        #analyzer.combination()
        #self.assertFalse(analyzer.combination())

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)