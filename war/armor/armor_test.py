import unittest
from armor import Armor


class TestArmorMethods(unittest.TestCase):
    def setUp(self):
        self.armor = Armor()

    def test_get_name(self):
        self.armor = Armor('name')
        print(self.armor, id(self.armor), id(self.armor.effects))
        self.assertEqual(self.armor.name, 'default_armor')

    def test_get_durability(self):
        self.armor = Armor('dur')
        print(self.armor, id(self.armor), id(self.armor.effects))
        self.assertEqual(self.armor.durability, 100)
        print('dur')

    def test_get_effects(self):
        self.armor = Armor('eff')
        print(self.armor, id(self.armor), id(self.armor.effects))
        self.assertEqual(self.armor.effects, [])
        print('get')

    def test_add_effect(self):
        self.armor = Armor('add')
        self.armor.add_effect('new_effect !')
        print(self.armor, id(self.armor), id(self.armor.effects))
        self.assertEqual(self.armor.effects, ['new_effect !'])
        print('add')

    def test_get_attack(self):
        pass


if __name__ == '__main__':
    unittest.main()
