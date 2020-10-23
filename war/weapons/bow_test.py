import unittest
from bow import Bow


class TestBowMethods(unittest.TestCase):
    
    def setUp(self):
        self.bow = Bow()

    def test_get_name(self):
        self.assertEqual(self.bow.name, 'Bow')

    def test_get_damage(self):
        self.assertEqual(self.bow.damage, 20)

    def test_set_damage(self):
        self.bow.damage = 10
        self.assertEqual(self.bow.damage, 100)   

    def test_get_accuracy(self):
        self.assertEqual(self.bow.accuracy, 10) 

    def test_set_accuracy(self):
        self.bow.accuracy = 20
        self.assertEqual(self.bow.accuracy, 20)   

    def test_set_accuracy_100(self):
        self.bow.accuracy = 150
        self.assertEqual(self.bow.accuracy, 100)   

    def test_attack(self):
        self.assertIn(self.bow.attack(), [20, 'Промах'])

    def test_le(self):
        b = Bow(damage=1)
        self.assertEqual(self.bow <= b, self.bow)

    def test_str(self):
        string = 'Название: Bow; Урон: 20'
        self.assertEqual(str(self.bow), string)


if __name__ == '__main__':
    unittest.main()