import unittest
print(dir())
from sword import Sword


class TestSwordMethods(unittest.TestCase):

    def setUp(self):
        self.sword = Sword()

    def test_get_name(self):
        self.assertEqual(self.sword.name, 'Sword')

    def test_get_damage(self):
        self.assertEqual(self.sword.damage, 10)

    def test_set_damage(self):
        self.sword.damage = 20
        self.assertEqual(self.sword.damage, 20)

    def test_get_durability(self):
        self.assertEqual(self.sword.durability, 1)

    def test_set_durability(self):
        self.sword.wearout()
        self.assertEqual(self.sword.durability, 0.9)

    def test_attack(self):
        self.assertEqual(self.sword.attack(), 10)

    def test_set_durability_after_attack(self):
        self.assertIn(self.sword.durability, [0.9, 1])

    def test_le(self):
        b = Sword(damage=20)
        self.assertEqual(self.sword <= b, True)

    def test_str(self):
        string = 'Название: Sword; Урон: 10'
        self.assertEqual(str(self.sword), string)


if __name__ == '__main__':
    unittest.main()
