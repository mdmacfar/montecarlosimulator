import unittest
import pandas as pd
import random
from typing import List
from mcs_pkg import Die, Game, Analyzer


class TestDie(unittest.TestCase):
    def setUp(self):
        self.die = Die([1,2,3,4,5,6])
        
    def test_init(self):
        # Test if the die initialize correctly
        self.assertEqual(self.die.faces, [1,2,3,4,5,6])
        self.assertEqual(self.die.weights, [1.0, 1.0, 1.0, 1.0, 1.0, 1.0])
        
    def test_change_weight(self):
        # Test if the weight of a face can be changed
        self.die.change_weight(1, 2.0)
        self.assertEqual(self.die.weights, [2.0, 1.0, 1.0, 1.0, 1.0, 1.0])
        self.die.change_weight(6, 0.5)
        self.assertEqual(self.die.weights, [2.0, 1.0, 1.0, 1.0, 1.0, 0.5])
        with self.assertRaises(ValueError):
            self.die.change_weight(7, 1.0)
        with self.assertRaises(ValueError):
            self.die.change_weight('A', 1.0)
        with self.assertRaises(ValueError):
            self.die.change_weight(1, 'A')
            
    def test_roll(self):
        # Test if the die roll correctly
        results = self.die.roll(1000)
        self.assertEqual(len(results), 1000)
        self.assertTrue(all([result in self.die.faces for result in results]))
        
    def test_show(self):
        # Test if the die show correctly
        self.die.show()

class TestGame(unittest.TestCase):
    def setUp(self):
        self.die1 = Die([1,2,3,4,5,6])
        self.die2 = Die([1,2,3,4,5,6])
        self.game = Game([self.die1, self.die2])
        
    def test_init(self):
        # Test if the game is initialized correctly
        self.assertEqual(self.game.dice, [self.die1, self.die2])
        self.assertEqual(self.game.results.shape, (0, 0))
        
    def test_play(self):
        # Test if the play method populates the dataframe correctly with valid faces
        self.game.play(1000)
        self.assertEqual(self.game.results.shape, (1000, 2))
        self.assertTrue(all([result in self.die1.faces for result in self.game.results['die_1']]))
        self.assertTrue(all([result in self.die2.faces for result in self.game.results['die_2']]))
        
    def test_show(self):
        # Test if the game shows correctly
        self.game.play(1000)
        self.game.show()
        self.game.show(wide=False)

class TestAnalyzer(unittest.TestCase):
    def setUp(self):
        self.die1 = Die([1,2,3,4,5,6])
        self.die2 = Die([1,2,3,4,5,6])
        self.game = Game([self.die1, self.die2])
        self.game.play(1000)
        self.analyzer = Analyzer(self.game)
        
    def test_init(self):
        # Test if the analyzer is initialized correctly
        self.assertEqual(self.analyzer.game, self.game)
        self.assertEqual(self.analyzer._infer_faces_dtype(), 'int')
        self.assertEqual(self.analyzer.face_count_results, None)
        self.assertEqual(self.analyzer.jackpot_results, None)
        self.assertEqual(self.analyzer.combo_results, None)
        
    def test_infer_faces_dtype(self):
        # Test when all die have integer faces 
        self.game = Game([Die([1, 2, 3]), Die([4, 5, 6])])
        self.analyzer = Analyzer(self.game)
        self.assertEqual(self.analyzer._infer_faces_dtype(), 'int')

        # Test when all die have string faces
        self.game = Game([Die(['A', 'B', 'C']), Die(['D', 'E', 'F'])])
        self.analyzer = Analyzer(self.game)
        self.assertEqual(self.analyzer._infer_faces_dtype(), 'str')

        # Test when all die have float faces
        self.game = Game([Die([1.1, 2.2, 3.3]), Die([4.4, 5.5, 6.6])])
        self.analyzer = Analyzer(self.game)
        self.assertEqual(self.analyzer._infer_faces_dtype(), 'float')

        # Test when die have mixed face types
        self.game = Game([Die([1, 2, 3]), Die(['A', 'B', 'C'])])
        with self.assertRaises(TypeError):
            self.analyzer = Analyzer(self.game)
            self.analyzer._infer_faces_dtype()

        # Test when die have unsupported face types
        class TestObject:
            pass   
        
        self.game = Game([Die([TestObject(), TestObject()]), Die([TestObject(), TestObject()])])
        with self.assertRaises(TypeError):
            self.analyzer = Analyzer(self.game)
            self.analyzer._infer_faces_dtype()
        
    def test_count_faces(self):
        # Test if the count_faces method populates the dataframe correctly
        self.analyzer.count_faces()
        self.assertEqual(self.analyzer.face_count_results.shape, (6, 1))