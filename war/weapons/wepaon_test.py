import unittest
from weapon import Weapon
import sys
sys.path.append('C:/Users/narut/practice_python/war')
from exceptions import NotRealizedMethodError

class TestWeaponMethods(unittest.TestCase):
    def setUp(self):
        self.weapon = Weapon()

    def test_get_name(self):
        self.assertEqual(self.weapon.name, 'Stick')

    def test_get_damage(self):
        with self.assertRaises(NotRealizedMethodError):
            self.weapon.damage

    def test_attack(self):
        with self.assertRaises(NotRealizedMethodError):
            self.weapon.attack(None)



if __name__ == '__main__':
    unittest.main()
